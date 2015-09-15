# -*- coding: utf-8 -*-

from src.utils.httpbase import HttpBaseHandler
from src.utils.tornado_extra import route
import src.pydev


@route('/(?!static).*.html')
class IndexHandler(HttpBaseHandler):
    def get(self, *args, **kwargs):
        with open(src.pydev.pathjoin('resources', 'templates', 'html', 'index.html'), 'r') as f:
            html = f.read()
        self.write(html)