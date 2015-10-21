# -*- coding: utf-8 -*-

import src.dao.info
import src.dao.audit
import src.dao.mongo_geo
import src.yunpian
import src.pydev.mysql
import src.pydev.config
import src.pydev.logger

conf = src.pydev.config.read_ini('core.ini')
logger = src.pydev.logger.create('daoaccess')


def list_wait_audit_shops():
    return src.dao.audit.list_wait_audit_shops()


def audit_shop_pass(shop_id):
    src.dao.audit.audit_shop_pass(shop_id)
    shop_info = src.dao.info.get_shop_info(shop_id)
    shop_accountinfo = src.dao.info.get_shopaccount_info(shop_id)
    src.dao.mongo_geo.remove_shop(shop_id)
    src.dao.mongo_geo.insert_shop(shop_id, shop_info['category_list'], shop_info['city_id'],
                                  float(shop_info['longitude']),
                                  float(shop_info['latitude']))
    src.yunpian.send_audit_shop_success(mobile=shop_accountinfo['contact_phone_no'],
                                        shopname=shop_info['shop_name'])
    return True


def audit_shop_not_pass(shop_id):
    return src.dao.audit.audit_shop_not_pass(shop_id)


def audit_shop_all():
    for i in list_wait_audit_shops():
        audit_shop_pass(i['shop_id'])
    return True


def list_audit_notpass_shops():
    conn = src.pydev.mysql.connection()
    cursor = conn.cursor()
    response = src.dao.audit.list_audit_notpass_shops(cursor)
    cursor.close()
    conn.close()
    return response

if __name__ == '__main__':
    r = list_audit_notpass_shops()
    print(r)