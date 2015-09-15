# -*- coding: utf-8 -*-
import pymongo

import src.pydev.config

conf = src.pydev.config.read_ini('core.ini')

client = pymongo.MongoClient(conf.get('mongo', 'host'), conf.getint('mongo', 'port'))
db = client.shop_address
places = db.places
places.create_index([('local', pymongo.GEOSPHERE)])