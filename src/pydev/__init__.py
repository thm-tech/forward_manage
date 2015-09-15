# -*- coding: utf-8 -*-

__author__ = 'Mohanson'

import os

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def pathjoin(*args):
    return os.path.join(PROJECT_PATH, *args)