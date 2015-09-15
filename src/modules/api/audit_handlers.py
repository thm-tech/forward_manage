# -*- coding: utf-8 -*-

import src.dao.info
import src.dao.audit
import src.dao.mongo_geo
import src.yunpian


def list_wait_audit_shops():
    return src.dao.audit.list_wait_audit_shops()


def audit_shop(shop_id):
    src.dao.audit.audit_shop(shop_id)
    shop_info = src.dao.info.get_shop_info(shop_id)
    shop_accountinfo = src.dao.info.get_shopaccount_info(shop_id)
    src.dao.mongo_geo.remove_shop(shop_id)
    src.dao.mongo_geo.insert_shop(shop_id, shop_info['category_list'], shop_info['city_id'],
                                  float(shop_info['longitude']),
                                  float(shop_info['latitude']))
    src.yunpian.send_audit_shop_success(mobile=shop_accountinfo['contact_phone_no'], shopname=shop_info['shop_name'])


def audit_shop_all():
    for i in list_wait_audit_shops():
        audit_shop(i['shop_id'])