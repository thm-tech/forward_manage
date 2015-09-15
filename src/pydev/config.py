# -*- coding: utf-8 -*-
import json

try:
    import configparser
except:
    import ConfigParser as configparser
from . import pathjoin


def read_ini(filename):
    path = pathjoin('resources', 'config', filename)
    conf = configparser.ConfigParser()
    conf.read(path)
    return conf


def read_json(filename):
    path = pathjoin('resources', 'config', filename)
    return json.load(path)