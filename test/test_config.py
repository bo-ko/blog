#!/usr/bin/env python3
#================================================================
#   Copyright (C) 2017 Sangfor Ltd. All rights reserved.
#   
#   > File Name：test_config.py
#   > Author：Bobo
#   > Created Time：2017-11-15 [14:05:39] (星期三)
#   > Mail：cgxpnwqb@gmail.com
#   > Describe: 
#================================================================

import sys
sys.path.append('../')

from handler.config import Config

cnf = Config("../conf/conf.ini")

name = cnf.get_config("mysqld", "NAME")

print(name)
