# -*- coding: utf-8 -*-

import tornado.template

import src.pydev

loader = tornado.template.Loader(src.pydev.pathjoin('resources', 'templates'))