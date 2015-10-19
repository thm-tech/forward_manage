# -*- coding: utf-8 -*-

import os

from tornado.web import authenticated

from src.utils.httpbase import HttpBaseHandler
from src.utils.tornado_extra import route, argument
import src.daoaccess.audit
import src.daoaccess.feedback
from src.pydev import pathjoin


@route(r'/audit/waits')
class AuditWaitsHandler(HttpBaseHandler):
    @authenticated
    def get(self, *args, **kwargs):
        shops = src.daoaccess.audit.list_wait_audit_shops()
        self.write({
            'shops': shops,
            'total_num': len(shops)
        })


@route(r'/audit/(.*)/pass')
class AuditPassHandler(HttpBaseHandler):
    @authenticated
    def put(self, shop_id, *args, **kwargs):
        r = src.daoaccess.audit.audit_shop_pass(shop_id)
        self.write({
            'is_success': r
        })


@route(r'/audit(.*)/notpass')
class AuditNotPassHandler(HttpBaseHandler):
    @authenticated
    def put(self, shop_id, *args, **kwargs):
        r = src.daoaccess.audit.audit_shop_not_pass(shop_id)
        self.write({
            'is_success': r
        })


@route(r'/documents')
class DocumentsHandler(HttpBaseHandler):
    @authenticated
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
    @authenticated
    @argument('_offset', '_limit')
    def get(self):
        response = src.daoaccess.feedback.get_user_feedbacks(int(self.arg.offset), int(self.arg.limit))
        self.write(response)


@route(r'/feedbacks/platform')
class FeedbacksPlatform(HttpBaseHandler):
    @authenticated
    @argument('_user_id')
    def get(self):
        response = src.daoaccess.feedback.get_platform_and_user_feedbacks(int(self.arg.user_id))
        self.write(response)

    @authenticated
    @argument('_user_id', '_content')
    def post(self):
        response = src.daoaccess.feedback.feedback_to_user(int(self.arg.user_id), self.arg.content)
        self.write(response)


@route(r'/login')
class LoginHandler(HttpBaseHandler):
    @argument('_user', '_pwd', 'remember')
    def post(self):
        if self.arg.user == 'admin' and self.arg.pwd == 'impower2015':
            if self.arg.remember == '1':
                self.set_secure_cookie(name='id', value='10000', expires_days=7)
            else:
                self.set_secure_cookie(name='id', value='10000', expires_days=1)
            self.write({
                'is_success': True
            })
        else:
            self.write({
                'is_success': False
            })


@route(r'/logout')
class LogoutHandler(HttpBaseHandler):
    def post(self):
        self.clear_cookie('id')
        self.write({
            'is_success': True
        })