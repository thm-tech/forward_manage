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
    sql = 'select * from fd_t_shopaccount where service_status = 1'
    row_counts = cursor.execute(sql)
    if row_counts:
        rows = list(cursor.fetchall())
        cursor.close()
        conn.close()

        return_rows = []
        for row in rows:
            info = {
                'shop_id': row['shop_id'],
                'contact_name': row['contact_name'],
                'contact_phone_no': row['contact_phone_no'],
                'contact_email': row['contact_email'],
                'contact_qq': row['contact_qq'],
                'service_balance': float(row['service_balance']),
                'service_deadline': src.utils.trans.datetime_to_string(row['service_deadline']),
                'service_status': row['service_status'],
                'portrait_url': src.utils.piclist_to_fulllist(row['portrait_url']),
            }
            return_rows.append(info)
        return return_rows
    else:
        cursor.close()
        conn.close()
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