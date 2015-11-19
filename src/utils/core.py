# -*- coding: utf-8 -*-

from src.settings import SETTINGS


def piclist_to_fulllist(piclist):
    if piclist:
        pl = piclist.split(',')
        if len(pl):
            return [SETTINGS['oss']['prefix'] + i for i in pl]
        else:
            return []
    else:
        return []