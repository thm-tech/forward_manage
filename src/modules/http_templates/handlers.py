# -*- coding: utf-8 -*-

from src.utils.httpbase import HttpBaseHandler
from src.utils.tornado_extra import route
import src.pydev


@route(r'/')
class IndexHandler(HttpBaseHandler):
    def get(self, *args, **kwargs):
        with open(src.pydev.pathjoin('resources', 'templates', 'html', 'index.html'), 'r') as f:
            html = f.read()
        self.write(html)

@route(r'/index.html')
class IndexHandler(HttpBaseHandler):
    def get(self, *args, **kwargs):
        with open(src.pydev.pathjoin('resources', 'templates', 'html', 'index.html'), 'r') as f:
            html = f.read()
        self.write(html)


@route(r'/audit.html')
class AuditHandler(HttpBaseHandler):
    def get(self, *args, **kwargs):
        with open(src.pydev.pathjoin('resources', 'templates', 'html', 'index.html'), 'r') as f:
            html = f.read()
        self.write(html)


@route(r'/feedback.html')
class FeedbackHandler(HttpBaseHandler):
    def get(self, *args, **kwargs):
        with open(src.pydev.pathjoin('resources', 'templates', 'html', 'index.html'), 'r') as f:
            html = f.read()
        self.write(html)


@route(r'/documents.html')
class DocumentsHandler(HttpBaseHandler):
    def get(self, *args, **kwargs):
        with open(src.pydev.pathjoin('resources', 'templates', 'html', 'index.html'), 'r') as f:
            html = f.read()
        self.write(html)


@route('/documents/(.*)')
class DocumentsContentHandler(HttpBaseHandler):
    def get(self, filename):
        with open(src.pydev.pathjoin('resources', 'documents', filename)) as f:
            text = f.read()
        self.write(text)