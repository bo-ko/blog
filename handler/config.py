#!/usr/bin/env python3
#================================================================
#   Copyright (C) 2017 Sangfor Ltd. All rights reserved.
#   
#   > File Name：config.py
#   > Author：Bobo
#   > Created Time：2017-11-09 [17:04:36] (星期四)
#   > Mail：cgxpnwqb@gmail.com
#   > Describe: 
#================================================================

import ConfigParser
import os
import sys

class Config:
    conf = ConfigParser.ConfigParser()
    def __init__(self, file):
        self.file = file

    def check_config_file(self, file):
        if os.path.exists(file):
            self.conf.read(file)
        else:
            print("Not find file %s !" %(file))
            sys.exit()
    
    def get_config(self, key, value):
        self.check_config_file(self.file)

        try:
            config = self.conf[key][value]
        except KeyError:
            print("Not find key %s or value! %s !" %(key, value))
            sys.exit()
        else:
            return config
