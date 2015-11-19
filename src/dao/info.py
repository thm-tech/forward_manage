# -*- coding: utf-8 -*-

import src.settings._mysql
import src.utils.trans
import src.utils


def get_shop_info(shop_id):
    sql = 'select * from fd_t_shop where shop_id = %s'
    params = [shop_id]
    r = src.settings._mysql.fetchone(sql, params)
    r['category_list'] = src.utils.trans.to_list(r['category_list'])
    r['pic_url_list'] = src.utils.piclist_to_fulllist(r['pic_url_list'])
    return r


def get_shopaccount_info(shop_id):
    sql = 'select * from fd_t_shopaccount where shop_id = %s'
    params = [shop_id]
    r = src.settings._mysql.fetchone(sql, params)
    r['portrait_url'] = src.utils.piclist_to_fulllist(r['portrait_url'])
    if r['portrait_url']:
        r['portrait_url'] = r['portrait_url'][0]
    else:
        r['portrait_url'] = None

    return r