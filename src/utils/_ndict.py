# -*- coding: utf-8 -*-

__author__ = 'Mohanson'


class ObjectDict(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        self[name] = value


def ndict(*args, **kwargs):
    return ObjectDict(*args, **kwargs)