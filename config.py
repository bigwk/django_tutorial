# coding: utf-8
# @Author   : wangkui
# @Time     : 2020/7/29 17:28
# @File     : config.py
# @Platform : PyCharm
import os
basedir = os.path.abspath(os.path.dirname(__file__))

try:
    import ConfigParser
except:
    import configparser as ConfigParser

config = ConfigParser.ConfigParser()


def load_service_config():
    config_filename = os.path.join(os.path.dirname(__file__), 'config.ini').replace(r'\\', '/')
    config.read(config_filename)
    return config


service_config = load_service_config()

class Config(object):
    SECRET_KEY = service_config.get('django_settings', 'secret_key')
    debug = True if service_config.get('django_settings', 'debug') == 'true' else False
    #
    database_name = service_config.get('database_settings', 'database_name')
    database = service_config.get('database_settings', 'database')
    user = service_config.get('database_settings', 'user')
    password = service_config.get('database_settings', 'password')
    host = service_config.get('database_settings', 'host')
    port = service_config.get('database_settings', 'port')

    time_zone = service_config.get('timezone_settings', 'time_zone')