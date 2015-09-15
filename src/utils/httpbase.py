# -*- coding: utf-8 -*-

import tornado.web


class HttpBaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(HttpBaseHandler, self).__init__(application, request, **kwargs)
        if 'Origin' in self.request.headers:
            self.add_header('Access-Control-Allow-Origin', self.request.headers['Origin'])
        elif 'Host' in self.request.headers:
            self.add_header('Access-Control-Allow-Origin', self.request.headers['Host'])
        self.add_header('Access-Control-Allow-Credentials', 'true')
        self.add_header('Access-Control-Allow-Methods', 'GET,POST,OPTIONS,PUT,DELETE')
        self.add_header('Access-Control-Allow-Headers',
                        'DNT,X-Mx-ReqToken,Keep-Alive,User-Agent,'
                        'X-Requested-With,If-Modified-Since,Cache-Control,Content-Type')
        self.add_header('Connection', 'keep-alive')

        # For tornado_extra.argument()
        self.arg = None

    def options(self, *args, **kwargs):
        pass