import logging

from Config.config_init import read_config
from common.random_def import read_yaml
from common.requests_def import requests_def

host = read_config("env", "test")
select_user_list_url = read_config("api", "select_user_list_url")


def select_uesr_list():
    body = requests_def(method="get", url=host + select_user_list_url,
                        params={'access_token': read_yaml("sccess_token.yaml"), "next_openid": ""})
    logging.info("调用【查询用户列表】接口，创建测试数据-接口响应结果：" + str(body.json()))
    open_list = body.json()['data']['openid']
    return open_list
