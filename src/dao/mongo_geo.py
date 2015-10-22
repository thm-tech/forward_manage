# -*- coding:utf8 - *-

import src.pydev.mongo
from src.pydev.logger import create

log_mongo = create('log_mongo')

places = src.pydev.mongo.places
log_mongo.info('connected mongodb success')


def remove_shop(shop_id):
    r = places.remove({'shop_id': int(shop_id)})
    return r


def insert_shop(shop_id, category_list, city_id, longitude, latitude):
    response = places.insert({'shop_id': int(shop_id),
                              'category_list': category_list,
                              'city_id': int(city_id),
                              'local': [float(longitude), float(latitude)]
                              })
    log_mongo.info('mongodb insert' + str(response))
    return response

insert_shop(10128, [206], 1048577, 117.286418, 31.837844)