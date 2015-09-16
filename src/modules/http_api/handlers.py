# -*- coding: utf-8 -*-

from src.utils.httpbase import HttpBaseHandler
from src.utils.tornado_extra import route
import src.modules.api.audit_handlers


@route('/audit/waits')
class AuditWaitsHandler(HttpBaseHandler):
    def get(self, *args, **kwargs):
        shops = src.modules.api.audit_handlers.list_wait_audit_shops()
        self.write({
            'shops': shops,
            'total_num': len(shops)
        })


@route('/audit/(.*)/pass')
class AuditPassHandler(HttpBaseHandler):
    def put(self, shop_id, *args, **kwargs):
        r = src.modules.api.audit_handlers.audit_shop_pass(shop_id)
        self.write({
            'is_success': r
        })


@route('/audit(.*)/notpass')
class AuditNotPassHandler(HttpBaseHandler):
    def put(self, shop_id, *args, **kwargs):
        r = src.modules.api.audit_handlers.audit_shop_not_pass(shop_id)
        self.write({
            'is_success': r
        })