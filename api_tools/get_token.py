# 在模块顶部定义全局变量
import logging

import pytest

from Config.config_init import read_config
from common.random_def import read_yaml
from common.requests_def import requests_def
from common.yaml_util import write_yaml


# host = read_config("env", "test")

def get_token():
    url = read_config("env", "test") + read_config("api", "get_token_url")
    params = {
        "grant_type": read_config("env", "grant_type"),
        "appid": read_config("env", "appid"),
        "secret": read_config("env", "secret")
    }
    # pass
    # print(url)

    resp = requests_def(method="get", url=url, params=params)
    write_yaml("ac.yaml", resp.json()["access_token"])
    logging.info(f"获取token成功：{resp.json()['access_token']}")
    # return resp.json()


# print(get_token())

@pytest.fixture
def read_token():
    return read_yaml("ac.yaml")


# 作用域范围变大 function=12 => class=3 => package=3 => session=3
@pytest.fixture(scope="session")
def yy_fixture():
    # 前置操作
    logging.info("这是前置代码 请进行操作：")
    # yield
    # # 后置操作
    # logging.info("这是后置代码 请进行操作：")
