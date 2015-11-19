# -*- coding: utf-8 -*-

import json
import codecs

from ._path import DIR
from ._logger import LOGGER_ROOT


settings = json.load(codecs.open(DIR.joinpath('resources', 'config', 'core.json').__str__(), encoding='utf-8'))

type = settings['type']
LOGGER_ROOT.info('This Project run in %s now' % type)

SETTINGS = settings[type]
