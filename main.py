# -*- coding: utf-8 -*-

import sys

sys.path.append('.')

import tornado
import tornado.ioloop
import tornado.httpserver
import tornado.wsgi
import tornado.web
from tornado.options import define, options
from tornado.web import StaticFileHandler

from src.utils.tornado_extra import urls, register

define('port', default=8888, help='run on the given port', type=int)

settings = {
    'xsrf_cookies': False,
    'login_url': '/',
    'debug': True,
    'cookie_secret': 'mohanson',
    'gzip': True,
    'static_path': './resources/templates/',
    'static_url_prefix': '/static/',
}

register('src.modules.http_api.handlers',
         'src.modules.http_templates.handlers')

for i in urls():
    print(i)

application = tornado.web.Application(urls(), **settings)
wsgi_application = tornado.wsgi.WSGIApplication(urls(), **settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
