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

import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('base.html')

