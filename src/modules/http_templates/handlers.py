# -*- coding: utf-8 -*-

from tornado.web import authenticated

from src.utils.httpbase import HttpBaseHandler
from src.utils.tornado_extra import route
from src.settings import DIR


@route(r'/')
class IndexHandler(HttpBaseHandler):
    @authenticated
    def get(self, *args, **kwargs):
        with open(DIR.joinpath('resources', 'templates', 'html', 'index.html').__str__(), 'r') as f:
            html = f.read()
        self.write(html)


@route(r'/index.html')
class IndexHandler(HttpBaseHandler):
    @authenticated
    def get(self, *args, **kwargs):
        with open(DIR.joinpath('resources', 'templates', 'html', 'index.html').__str__(), 'r') as f:
            html = f.read()
        self.write(html)


@route(r'/audit.html')
class AuditHandler(HttpBaseHandler):
    @authenticated
    def get(self, *args, **kwargs):
        with open(DIR.joinpath('resources', 'templates', 'html', 'index.html').__str__(), 'r') as f:
            html = f.read()
        self.write(html)


@route(r'/feedback.html')
class FeedbackHandler(HttpBaseHandler):
    @authenticated
    def get(self, *args, **kwargs):
        with open(DIR.joinpath('resources', 'templates', 'html', 'index.html').__str__(), 'r') as f:
            html = f.read()
        self.write(html)


@route(r'/documents.html')
class DocumentsHandler(HttpBaseHandler):
    def get(self, *args, **kwargs):
        with open(DIR.joinpath('resources', 'templates', 'html', 'index.html').__str__(), 'r') as f:
            html = f.read()
        self.write(html)


@route(r'/login.html')
class LoginHandler(HttpBaseHandler):
    def get(self, *args, **kwargs):
        with open(DIR.joinpath('resources', 'templates', 'html', 'index.html').__str__(), 'r') as f:
            html = f.read()
        self.write(html)


@route('/documents/(.*)')
class DocumentsContentHandler(HttpBaseHandler):
    def get(self, filename):
        with DIR.joinpath('resources', 'documents', filename).open() as f:
            text = f.read()
        self.write(text)