# -*- coding:utf8 - *-

import src.pydev.mongo

places = src.pydev.mongo.places


def remove_shop(shop_id):
    r = places.remove({'shop_id': int(shop_id)})
    return r


def insert_shop(shop_id, category_list, city_id, longitude, latitude):
    return places.insert({'shop_id': int(shop_id),
                          'category_list': category_list,
                          'city_id': int(city_id),
                          'local': [float(longitude), float(latitude)]
                          })