#!/usr/bin/env python3
#================================================================
#   Copyright (C) 2017 Sangfor Ltd. All rights reserved.
#   
#   > File Name：url.py
#   > Author：Bobo
#   > Created Time：2017-11-09 [17:05:47] (星期四)
#   > Mail：cgxpnwqb@gmail.com
#   > Describe: 
#================================================================

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from handler.index import IndexHandler

url=[
    (r'/', IndexHandler),

    ]
