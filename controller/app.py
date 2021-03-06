#!/usr/bin/env python3
#================================================================
#   Copyright (C) 2017 Sangfor Ltd. All rights reserved.
#   
#   > File Name：app.py
#   > Author：Bobo
#   > Created Time：2017-11-09 [17:04:17] (星期四)
#   > Mail：cgxpnwqb@gmail.com
#   > Describe: 
#================================================================

from url import url

import tornado.web
import os

setting = dict(
    template_path=os.path.join(os.path.dirname(__file__),"template"),
    static_path=os.path.join(os.path.dirname(__file__),"static"),
    )

application = tornado.web.Application(
    handlers=url,
    **setting
    )

