# -*- coding: utf-8 -*-
import functools
import inspect
import re

__author__ = 'Mohanson'


class MetaCondition(object):
    def __init__(self, fun, des):
        self.fun = fun
        self.des = des

    def __and__(self, other):
        def paramscheckfunc(x):
            if not self.fun(x) or not other.fun(x):
                return False
            return True

        return MetaCondition(paramscheckfunc, des='[' + self.des + ' & ' + other.des + ']')

    def __or__(self, other):
        def paramscheckfunc(x):
            if self.fun(x) or other.fun(x):
                return True
            return False

        return MetaCondition(paramscheckfunc, des='(' + self.des + ' | ' + other.des + ')')

    def __call__(self, args):
        return self.fun(args)

    def __str__(self):
        return self.des


def concrete_is_metacondition(condition):
    return condition


def concrete_is_class(condition):
    fun = lambda _: isinstance(_, condition)
    des = 'type %s' % str(condition)
    return MetaCondition(fun, des)


def concrete_is_fun(condition):
    fun = condition
    des = '%s(_)' % condition.__name__
    return MetaCondition(fun, des)


def concrete_is_str(condition):
    if condition[0] == condition[-1] == '/':
        fun = lambda _: isinstance(_, str) and re.match(condition[1:-1], _) is not None
        des = 're.match(%s)' % condition[1:-1]
    else:
        fun = lambda _: eval(condition)
        des = condition
    return MetaCondition(fun, des)


def concrete_is_none():
    fun = lambda _: _ is None
    des = 'None'
    return MetaCondition(fun, des)


def concrete_is_list(conditions):
    c = get_meta_condition(conditions.pop(0))
    for condition in conditions:
        c &= get_meta_condition(condition)
    return c


def concrete_is_tuple(conditions):
    c = get_meta_condition(conditions[0])
    for condition in conditions[1:]:
        c |= get_meta_condition(condition)
    return c


# Trans User Check Rules To MetaCondition Class
def get_meta_condition(condition):
    if condition is None:
        return concrete_is_none()
    if isinstance(condition, MetaCondition):
        return concrete_is_metacondition(condition)
    if inspect.isclass(condition):
        return concrete_is_class(condition)
    if hasattr(condition, '__call__'):
        return concrete_is_fun(condition)
    if isinstance(condition, str):
        return concrete_is_str(condition)
    if isinstance(condition, list):
        return concrete_is_list(condition)
    if isinstance(condition, tuple):
        return concrete_is_tuple(condition)
    raise ErrorParamsCheck('paramscheck params error!')


# Paramscheck decorator
def paramscheck(*aargs, **kkwargs):
    aargs = list(map(get_meta_condition, aargs))
    kkwargs = dict([(kkwarg, get_meta_condition(kkwargs[kkwarg])) for kkwarg in kkwargs])

    def generator(func):
        params_func_dict = _params_to_paramsdict(func, aargs, kkwargs, False)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            paramsdict = _params_to_paramsdict(func, args, kwargs, True)
            for param in params_func_dict:
                fun = params_func_dict[param]
                if param in paramsdict and fun(paramsdict[param]) is False:
                    raise ErrorParamsCheck(
                        'params <%s> was <%s: type %s> but it should be: %s' % (
                            param, paramsdict[param], type(paramsdict[param]), fun))
            return func(*args, **kwargs)

        return wrapper

    return generator


def _params_to_paramsdict(func, args, kwargs, is_default):
    """
    trans func params to dict(key, value) type
    """
    result = {}
    iargs, ivarargs, ikeywords, defaults = inspect.getargspec(func)[:4]

    # set default key/value in paramsdict if is_default
    if defaults and is_default:
        for index, default in enumerate(defaults[::-1]):
            result[iargs[-(index + 1)]] = default

    # set args value in paramsdict
    for index, arg in enumerate(args):
        result[iargs[index]] = args[index]

    # set kwargs key/value in paramsdict
    result.update(kwargs)

    return result


class Error(Exception):
    pass


class ErrorParamsCheck(Error):
    def __init__(self, des):
        self.des = des

    def __str__(self):
        return self.des