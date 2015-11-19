# -*- coding: utf-8 -*-
from __future__ import print_function
import sys


class Error(Exception):
    pass


class _Option:
    UNSET = object()

    def __init__(self, name, alias, type, default, help):
        self.name = name
        self.alias = alias
        self.type = type
        self.default = default
        self.help = help

        self._value = _Option.UNSET

    def value(self):
        return self.default if self._value is _Option.UNSET else self._value

    def parse(self, value):
        _parse = {

        }.get(self.type, self.type)
        self._value = _parse(value)
        return self.value()

    def set(self, value):
        self._value = value


class OptionParser:
    def __init__(self):
        self.__dict__['_options'] = {}
        self.__dict__['_alias'] = {}
        self.__dict__['_commands'] = {}

        self.define('help', bool, 'h', False, 'help document')

    def __getattr__(self, name):
        if isinstance(self._options.get(name), _Option):
            return self._options[name].value()
        raise AttributeError("Unrecognized option %r" % name)

    def commands(self):
        return self._commands

    def items(self):
        return [(name, opt.value()) for name, opt in self._options.items()]

    def groups(self):
        return set(opt.group_name for opt in self._options.values())

    def group_dict(self, group):
        return dict(
            (name, opt.value()) for name, opt in self._options.items()
            if not group or group == opt.group_name)

    def as_dict(self):
        return dict(
            (name, opt.value()) for name, opt in self._options.items())

    def print_usage(self):
        print('Usage:')
        print('    prefix [options] [command] [args]\n')
        print('Options:')
        for i in self._options.values():
            pre = '    -%s --%s' % (i.alias, i.name)
            pre += ' ' * (35 - len(pre))
            print(pre, end='')
            print(i.help)

    def define(self, name, type, alias=None, default=None, help=None):
        if name in self._options or alias in self._alias:
            raise Error("Option %s already defined" % name)
        self._options[name] = _Option(name, alias, type, default, help)
        self._alias[alias] = name

    def parse_command_line(self):
        argvs = sys.argv[1:]
        for argv in argvs:
            if argv in ('-', '--'):
                continue
            if argv.startswith('-'):
                if argv.startswith('--'):
                    key, _, value = argv[2:].partition('=')
                    value = value or True
                    if key not in self._options:
                        raise ('Undefined Option: %s' % argv)
                else:
                    key, value = argv[1:2], argv[2:] or True
                    if key not in self._alias:
                        raise ('Undefined Option: %s' % argv)
                    key = self._alias[key]
                if key == 'help':
                    self.print_usage()
                    sys.exit(0)
                self._options[key].parse(value)
            else:
                self._commands.append(argv)


options = OptionParser()