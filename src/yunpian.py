# -*- coding: utf-8 -*-

import httplib
import urllib
import random
import json

import src.pydev.config


conf = src.pydev.config.read_ini('core.ini')

host = "yunpian.com"
port = 80
version = "v1"
user_get_uri = "/" + version + "/user/get.json"
sms_tpl_send_uri = "/" + version + "/sms/tpl_send.json"

apikey = conf.get('yunpian', 'apikey')
company = conf.get('yunpian', 'company')


def combine_tpl_value(**kwargs):
    tpl_value = []
    for kwarg in kwargs:
        tpl_value.append('#%s#=%s' % (kwarg, kwargs[kwarg]))
    tpl_value = '&'.join(tpl_value)
    return tpl_value


def send_message(mobile, tpl_id, **kwargs):
    tpl_value = combine_tpl_value(**kwargs)
    params = urllib.urlencode({'apikey': apikey, 'tpl_id': tpl_id, 'tpl_value': tpl_value, 'mobile': mobile})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(host, port=port, timeout=30)
    conn.request("POST", sms_tpl_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


def send_phone_captcha(mobile):
    code = random.randint(100000, 999999)
    r = json.loads(send_message(mobile=mobile, tpl_id=2, code=code, company=company))
    return r


def send_audit_shop_success(mobile, shopname):
    r = send_message(mobile=mobile, tpl_id=865727, shopname=shopname)
    return r


if __name__ == '__main__':
    r = send_audit_shop_success('18756967287', '小苹果2')
    print(r)