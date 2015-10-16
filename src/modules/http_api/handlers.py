# -*- coding: utf-8 -*-

import os

from src.utils.httpbase import HttpBaseHandler
from src.utils.tornado_extra import route, argument
import src.daoaccess.audit
import src.daoaccess.feedback
from src.pydev import pathjoin


@route(r'/audit/waits')
class AuditWaitsHandler(HttpBaseHandler):
    def get(self, *args, **kwargs):
        shops = src.daoaccess.audit.list_wait_audit_shops()
        self.write({
            'shops': shops,
            'total_num': len(shops)
        })


@route(r'/audit/(.*)/pass')
class AuditPassHandler(HttpBaseHandler):
    def put(self, shop_id, *args, **kwargs):
        r = src.daoaccess.audit.audit_shop_pass(shop_id)
        self.write({
            'is_success': r
        })


@route(r'/audit(.*)/notpass')
class AuditNotPassHandler(HttpBaseHandler):
    def put(self, shop_id, *args, **kwargs):
        r = src.daoaccess.audit.audit_shop_not_pass(shop_id)
        self.write({
            'is_success': r
        })


@route(r'/documents')
class DocumentsHandler(HttpBaseHandler):
    def get(self):
        return_list = []
        documents_dir = pathjoin('resources', 'documents')
        for i in os.listdir(documents_dir):
            return_list.append(os.path.basename(i))
        self.write({
            'documents': return_list
        })


@route(r'/feedbacks/user')
class FeedbacksFromUser(HttpBaseHandler):
    @argument('_offset', '_limit')
    def get(self):
        response = src.daoaccess.feedback.get_user_feedbacks(int(self.arg.offset), int(self.arg.limit))
        self.write(response)


@route(r'/feedbacks/platform')
class FeedbacksPlatform(HttpBaseHandler):
    @argument('_user_id')
    def get(self):
        response = src.daoaccess.feedback.get_platform_and_user_feedbacks(int(self.arg.user_id))
        self.write(response)

    @argument('_user_id', '_content')
    def post(self):
        response = src.daoaccess.feedback.feedback_to_user(int(self.arg.user_id), self.arg.content)
        self.write(response)