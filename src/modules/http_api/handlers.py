# -*- coding: utf-8 -*-

from src.utils.httpbase import HttpBaseHandler
from src.utils.tornado_extra import route, argument, argument_json


@route('/audit/(.*)')
class AuditHandler(HttpBaseHandler):
    def get(self, *args, **kwargs):
        self.write('Hello World!')

    def post(self, *args, **kwargs):
        pass