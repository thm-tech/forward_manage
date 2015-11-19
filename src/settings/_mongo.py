# -*- coding: utf-8 -*-
import pymongo

from ._settings import SETTINGS


client = pymongo.MongoClient(SETTINGS['mongo']['host'], SETTINGS['mongo']['port'])
db = client.shop_address
places = db.places
places.create_index([('local', pymongo.GEOSPHERE)])

MONGO_DATABASE_PLACES = places