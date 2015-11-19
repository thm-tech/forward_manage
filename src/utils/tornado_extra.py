# -*- encoding: utf-8 -*-

__author__ = 'Mohanson'

import json
import functools
from collections import namedtuple

from tornado.web import MissingArgumentError


class Error(Exception):
    pass


class ErrorTornadoExtra(Error):
    def __init__(self, des):
        self.des = des

    def __str__(self):
        return self.des


def argument(*margs):
    def decorator(func):

        @functools.wraps(func)
        def wapper(self, *args, **kwargs):
            must = []
            maybe = []
            if isinstance(margs, str):
                must.append(margs[0]) if margs[0].startswith('_') else maybe.append(margs[0])
            else:
                for marg in margs:
                    must.append(marg[1:]) if marg.startswith('_') else maybe.append(marg)
            nametype = namedtuple('nametype', ' '.join(must + maybe))

            try:
                must_value = [self.get_argument(i) for i in must]
            except MissingArgumentError:
                self.write(dict(is_success=False,
                                des='Missing argument what is necessary, You should read API file',
                                must=must,
                                maybe=maybe))
                return
            except Exception:
                self.write(dict(is_success=False, des='Do not ask me, I also do not know why it happend'))
                return
            maybe_value = [self.get_argument(i, None) for i in maybe]
            self.arg = nametype(*(must_value + maybe_value))
            func(self, *args, **kwargs)

        return wapper

    return decorator


def argument_json(*margs):
    from collections import namedtuple

    def decorator(func):

        @functools.wraps(func)
        def wapper(self, *args, **kwargs):
            must = []
            maybe = []
            data = json.loads(self.request.body)
            if isinstance(margs, str):
                must.append(margs[0]) if margs[0].startswith('_') else maybe.append(margs[0])
            else:
                for marg in margs:
                    must.append(marg[1:]) if marg.startswith('_') else maybe.append(marg)
            nametype = namedtuple('nametype', ' '.join(must + maybe))

            try:
                must_value = [data[i] for i in must]
            except:
                self.write(dict(is_success=False,
                                des='Missing argument what is necessary, You should read API file',
                                must=must,
                                maybe=maybe))
                return

            maybe_value = [data.get(i) for i in maybe]

            self.arg = nametype(*(must_value + maybe_value))
            func(self, *args, **kwargs)

        return wapper

    return decorator


__urls = []


def urls():
    return __urls


def route(url, outurls=list()):
    global __urls
    if url in [u[0] for u in __urls]:
        raise ErrorTornadoExtra('%s already register')

    def decorator(klass):
        __urls.append((url, klass))
        outurls.append((url, klass))
        return klass

    return decorator


def register(*args):
    for arg in args:
        __import__(arg)