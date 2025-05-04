import logging

import allure
import pytest

from Config.config_init import read_config
from api_tools.get_token import read_token
from common.requests_def import requests_def
from common.yaml_util import read_testCase

host = read_config("env", "test")


@allure.epic("微信项目")
@allure.feature('客服管理功能')
class Test_upload_head:

    @allure.story("上传头像接口用例")
    @pytest.mark.parametrize('case', read_testCase("kf_mannage/upload_head_img.yaml"))
    def test_upload_head(self, case, read_token):
        with allure.step("组装参数"):
            # url = f"{host}{case['url']}?access_token={read_token}&kf_account={case['params']['kf_account']}"
            # param = case['data']
            # file_path = read_config("path", "Data_path")
            # media_ = file_path + "/imgs/" + case["files"]['media']
            media = read_config("path", "imgs_path") + case["files"]['media']

            # files = {'file': (case["files"]['media'], open(media, 'rb'))}
            files = {'file': open(media, 'rb')}
            # logging.debug(f"------------param--{param}------------------")

        with allure.step("调用接口"):
            resp = requests_def(method=case['method'], url=host + case['url'],
                                params={
                                    "access_token": read_token,
                                    'kf_account': case['params']['kf_account']
                                }, files=files)
            # assert_resp['statusCode']= resp.status_code
            logging.debug(f"----------resp----{resp.json()}------------------")
            logging.debug(f"----------Expected----{case['excepted']}------------------")

            with allure.step("结果验证"):
                assert case["excepted"]['statusCode'] == resp.status_code
            assert case.get("excepted", {}).get("errcode") == resp.json()['errcode']
