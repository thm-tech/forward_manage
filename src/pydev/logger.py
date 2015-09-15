# -*- coding: utf-8 -*-
import os

__author__ = 'Mohanson'

import logging
import logging.handlers
import sys

from . import pathjoin

LOG_BASEDIR = pathjoin('resources', 'output', 'log')

LOGGER_LEVEL = logging.DEBUG

FORMATTER = '[%(asctime)s %(levelname)s %(filename)s:%(lineno)d] %(message)s'

MAXBYTES = 1024 * 1024

BACKUPCOUNT = 5

ENCODING = 'utf-8'


def create(name='standard'):
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)
    formatter = logging.Formatter(FORMATTER)

    file_handler = logging.handlers.RotatingFileHandler(os.path.join(LOG_BASEDIR, name + '.log'),
                                                        mode='a', maxBytes=MAXBYTES, backupCount=BACKUPCOUNT,
                                                        encoding=ENCODING, delay=0)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(LOGGER_LEVEL)

    log.addHandler(file_handler)
    log.addHandler(stream_handler)
    return log