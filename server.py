#!/usr/bin/env python3
#================================================================
#   Copyright (C) 2017 Sangfor Ltd. All rights reserved.
#   
#   > File Name：server.py
#   > Author：Bobo
#   > Created Time：2017-11-09 [17:06:43] (星期四)
#   > Mail：cgxpnwqb@gmail.com
#   > Describe: 
#================================================================

import tornado.ioloop
import tornado.options
import tornado.httpserver

import sys

from handler.app import application

from tornado.options import define,options
define("port",default=8888,help="run on th given port",type=int)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print('Development server is running at http://127.0.0.1:%s/' % options.port)
    print('Quit the server with Control-C')
    tornado.ioloop.IOLoop.instance().start()

if __name__=="__main__":
    main()
