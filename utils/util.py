# -*- coding: utf-8 -*-
# @Time    : 2020/10/26 4:56 下午
# @Author  : JiangYanQun
# @File    : util.py


import configparser
import os


def get_config(config_file_path):
    """
    读取config内容
    """
    config = configparser.ConfigParser()
    config.read(config_file_path, encoding='utf8')
    return config


config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config.cfg")
print(config_path)
