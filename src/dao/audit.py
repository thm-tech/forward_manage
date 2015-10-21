# -*- coding: utf-8 -*-

import datetime

import src.pydev.mysql
import src.define
import src.pydev.config
import src.pydev.logger
import src.utils
import src.utils.trans

conf = src.pydev.config.read_ini('core.ini')
logger = src.pydev.logger.create('dao')


def list_wait_audit_shops():
    conn = src.pydev.mysql.connection()
    cursor = conn.cursor()
    sql = """
        SELECT DISTINCT
        fd_t_shopaccount.shop_id,
        fd_t_shopaccount.contact_name,
        fd_t_shopaccount.contact_phone_no,
        fd_t_shopaccount.contact_email,
        fd_t_shopaccount.contact_qq,
        fd_t_shop.brand_name,
        fd_t_shop.shop_name,
        fd_t_shop.business_hours,
        fd_t_shop.telephone_no,
        fd_t_shop.city_id,
        fd_t_shop.district_id,
        fd_t_shop.business_area,
        fd_t_shop.address,
        fd_t_shop.category_list,
        fd_t_citycode.city_name,
        fd_t_category.name
        FROM
        fd_t_shopaccount
        LEFT JOIN fd_t_shop ON fd_t_shopaccount.shop_id = fd_t_shop.shop_id
        LEFT JOIN fd_t_citycode ON fd_t_shop.city_id = fd_t_citycode.city_id
        LEFT JOIN fd_t_category ON fd_t_shop.category_list = fd_t_category.id
        WHERE
        fd_t_shopaccount.service_status = 1"""
    row_counts = cursor.execute(sql)
    if row_counts:
        rows = list(cursor.fetchall())
        cursor.close()
        conn.close()

        return_rows = []
        for row in rows:
            info = {
                'shop_id': row['shop_id'],
                'shop_name': row['shop_name'],

                'brand_name': row['brand_name'],
                'business_hours': row['business_hours'],
                'telephone_no': row['telephone_no'],
                'city_id': row['city_id'],
                'city_name': row['city_name'],
                'district_id': row['district_id'],
                'business_area': row['business_area'],
                'address': row['address'],
                'category_list': row['category_list'],

                'contact_name': row['contact_name'],
                'contact_phone_no': row['contact_phone_no'],
                'contact_email': row['contact_email'],
                'contact_qq': row['contact_qq'],
                # 'service_balance': float(row['service_balance']),
                # 'service_deadline': src.utils.trans.datetime_to_string(row['service_deadline']),
                # 'service_status': row['service_status'],
                # 'portrait_url': src.utils.piclist_to_fulllist(row['portrait_url']),
            }
            return_rows.append(info)
        return return_rows
    else:
        cursor.close()
        conn.close()
        return []


def list_audit_notpass_shops(cursor):
    sql = """
        SELECT DISTINCT
        fd_t_shopaccount.shop_id,
        fd_t_shopaccount.contact_name,
        fd_t_shopaccount.contact_phone_no,
        fd_t_shopaccount.contact_email,
        fd_t_shopaccount.contact_qq,
        fd_t_shop.brand_name,
        fd_t_shop.shop_name,
        fd_t_shop.business_hours,
        fd_t_shop.telephone_no,
        fd_t_shop.city_id,
        fd_t_shop.district_id,
        fd_t_shop.business_area,
        fd_t_shop.address,
        fd_t_shop.category_list,
        fd_t_citycode.city_name,
        fd_t_category.name
        FROM
        fd_t_shopaccount
        LEFT JOIN fd_t_shop ON fd_t_shopaccount.shop_id = fd_t_shop.shop_id
        LEFT JOIN fd_t_citycode ON fd_t_shop.city_id = fd_t_citycode.city_id
        LEFT JOIN fd_t_category ON fd_t_shop.category_list = fd_t_category.id
        WHERE
        fd_t_shopaccount.service_status = 4"""
    row_counts = cursor.execute(sql)
    if row_counts:
        rows = list(cursor.fetchall())

        return_rows = []
        for row in rows:
            info = {
                'shop_id': row['shop_id'],
                'shop_name': row['shop_name'],

                'brand_name': row['brand_name'],
                'business_hours': row['business_hours'],
                'telephone_no': row['telephone_no'],
                'city_id': row['city_id'],
                'city_name': row['city_name'],
                'district_id': row['district_id'],
                'business_area': row['business_area'],
                'address': row['address'],
                'category_list': row['category_list'],

                'contact_name': row['contact_name'],
                'contact_phone_no': row['contact_phone_no'],
                'contact_email': row['contact_email'],
                'contact_qq': row['contact_qq'],
            }
            return_rows.append(info)
        return return_rows
    else:
        return []


def audit_shop_pass(shop_id):
    conn = src.pydev.mysql.connection()
    cursor = conn.cursor()
    # set fd_t_shopaccount
    sql = 'update fd_t_shopaccount set service_deadline = %s, service_status = %s where shop_id = %s'
    params = [datetime.datetime.now() + datetime.timedelta(days=365), src.define.SERVICE_STATUS.NORMAL, shop_id]
    row_count = cursor.execute(sql, params)

    # set fd_t_fansmessage
    sql2 = 'update fd_t_fansmessageconfig set ' \
           'current_p2p_count = %s, p2p_remain_count = %s, next_p2p_count = %s, ' \
           'current_mass_count = %s, mass_remain_count = %s, next_mass_count = %s where shop_id = %s'
    params2 = [conf.get('fansmessageconfig', 'current_p2p_count'),
               conf.get('fansmessageconfig', 'p2p_remain_count'),
               conf.get('fansmessageconfig', 'next_p2p_count'),
               conf.get('fansmessageconfig', 'current_mass_count'),
               conf.get('fansmessageconfig', 'mass_remain_count'),
               conf.get('fansmessageconfig', 'next_mass_count'),
               shop_id
               ]
    row_count2 = cursor.execute(sql2, params2)
    logger.info('audit shop: shop_id: %s, fd_t_shopaccount row count:%s, fd_t_fansmessageconfig row count:%s' % (
        shop_id, row_count, row_count2))
    cursor.close()
    conn.commit()
    conn.close()
    return row_count, row_count2


def audit_shop_not_pass(shop_id):
    conn = src.pydev.mysql.connection()
    cursor = conn.cursor()
    # set fd_t_shopaccount
    sql = 'update fd_t_shopaccount set service_status = %s where shop_id = %s'
    params = [src.define.SERVICE_STATUS.AUDIT_NOT_PASS, shop_id]
    row_count = cursor.execute(sql, params)
    logger.info('audit shop not pass: shop_id: %s, fd_t_shopaccount row count:%s' % (shop_id, row_count, ))
    cursor.close()
    conn.commit()
    conn.close()
    return True


def audit_shop_all():
    sl = list_wait_audit_shops()
    for i in sl:
        audit_shop_pass(i['shop_id'])
    return len(sl)


if __name__ == '__main__':
    conn = src.pydev.mysql.connection()
    cursor = conn.cursor()
    print(list_audit_notpass_shops(cursor))