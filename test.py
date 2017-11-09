#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2017 Sangfor Ltd. All rights reserved.
#   
#   > File Name：poemmaker.py
#   > Author：Bobo
#   > Created Time：2017-10-10 [09:38:27] (星期二)
#   > Mail：cgxpnwqb@gmail.com
#   > Describe: 
#================================================================

import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define ("port", default=8888, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('base.html')
class TestHandler(tornado.web.RequestHandler):
    def get(self,num):
        self.write(num)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
        (r'/', IndexHandler),
        (r'/testpage/(?P<num>\d*)',TestHandler)
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static")
        )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
