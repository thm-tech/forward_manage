# -*- coding: utf-8 -*-

import src.pydev.config

conf = src.pydev.config.read_ini('core.ini')


def piclist_to_fulllist(piclist):
    if piclist:
        pl = piclist.split(',')
        if len(pl):
            return [conf.get('oss', 'prefix') + i for i in pl]
        else:
            return []
    else:
        return []