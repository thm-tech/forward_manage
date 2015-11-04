# -*- coding:utf8 - *-

from src.settings import MONGO_DATABASE_PLACES, LOGGER_MONGO


LOGGER_MONGO.info('connected mongodb success')


def remove_shop(shop_id):
    r = MONGO_DATABASE_PLACES.remove({'shop_id': int(shop_id)})
    return r


def insert_shop(shop_id, category_list, city_id, longitude, latitude):
    response = MONGO_DATABASE_PLACES.insert({'shop_id': int(shop_id),
                              'category_list': category_list,
                              'city_id': int(city_id),
                              'local': [float(longitude), float(latitude)],
                              'weights': 0.01,
                              })
    LOGGER_MONGO.info('mongodb insert' + str(response))
    return response


if __name__ == '__main__':
    import random

    for i in MONGO_DATABASE_PLACES.find({}):
        MONGO_DATABASE_PLACES.update_one({'shop_id': i['shop_id']}, {'$set': {'weight': random.random() * 100}})