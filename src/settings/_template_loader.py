# -*- coding: utf-8 -*-
import tornado
import tornado.template

from ._path import DIR


TEMPLATE_LOADER = tornado.template.Loader(DIR.joinpath('resources', 'templates').__str__())