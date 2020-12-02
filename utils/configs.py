
import logging
import configparser

import os
from typing import OrderedDict

def get_config(key, default = None):
    config = None
    value = os.getenv(key)
    if value is None:
        if config is None:
            config = _read_config_ini("config.ini")
        return config["config"][key.lower()]
    return default


def _read_config_ini(config_path):
    u""" 读取配置文件

        :param str config_path: 配置文件路径

        :return: dict config_data
    """
    config_data = OrderedDict(dict())
    if not config_path or not os.path.exists(config_path):
        logging.error("配置文件[%s]为空或不存在", config_path)
        return config_data

    try:
        config = configparser.ConfigParser()
        config.readfp(open(r'%s' % config_path))
        for section in config.sections():
            config_data[section] = OrderedDict(dict())
            for key, val in config.items(section):
                config_data[section][key] = val
    except Exception as e:
        logging.error("配置文件[%s]无法正常解析,请检查!", config_path)
    return config_data
