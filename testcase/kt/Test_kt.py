import logging

import allure
import allure_pytest
import pytest
import requests

from Config.config_init import read_config
from api_tools.get_token import read_token, yy_fixture
from common.requests_def import requests_def
from common.yaml_util import read_testCase, read_yamlFile

host = read_config("env", "test")


@allure.epic("微信项目")
@allure.feature('客服管理功能')
class Test_kf:

    @allure.story("创建客服账号接口用例")
    @pytest.mark.parametrize('case', read_testCase("kf_mannage/create_kf.yaml"))
    def test_create(self, case, read_token):
        with allure.step("组装参数"):
            # token0 = read_token()
            # token0 = read_yamlFile("param/ac.yaml")
            # url = host + case['url'] + '?access_token=' + token0
            url = f"{host}{case['url']}?access_token={read_token}"
            param = case['data']
            logging.debug(f"------------param--{param}------------------")

        with allure.step("调用接口"):
            resp = requests_def(method=case['method'], url=url, json=param)
            resp.json()
            # assert_resp['statusCode']= resp.status_code
            logging.debug(f"----------resp----{resp.json()}------------------")
            logging.debug(f"----------Expected----{case['excepted']}------------------")

        with allure.step("结果验证"):
            assert case["excepted"]['statusCode'] == resp.status_code
            assert case.get("excepted", {}).get("errcode") == resp.json()['errcode']

    @allure.story("查询客服账号接口用例")
    @pytest.mark.parametrize('case', read_testCase("kf_mannage/get_kf_list.yaml"))
    def test_query(self, case, read_token):
        with allure.step("组装参数"):
            url = f"{host}{case['url']}?access_token={read_token}"
        with allure.step("调用接口"):
            resp = requests_def(method=case['method'], url=url)
            resp.json()
            logging.debug(f"----------query  resp----{resp.json()}------------------")
            logging.debug(f"----------query Expected----{case['excepted']}------------------")

        with allure.step("结果验证"):
            exist_count = 0
            for kt in resp.json()['kf_list']:  # 11 11 33
                if kt['kf_account'] in case["excepted"]['kf_account_name']:  # 11 22
                    exist_count = exist_count + 1

            assert exist_count == len(case["excepted"]['kf_account_name'])

            all_exist = True
            target_list = case["excepted"]['kf_account_name']
            dict_list = resp.json()["kf_list"]
            for target in target_list:
                if target not in [d['kf_account'] for d in dict_list]:
                    all_exist = False
                    break
            print(all_exist)

            assert case["excepted"]['statusCode'] == resp.status_code
            assert all_exist
            # assert case.get("excepted", {}).get("errcode") == resp.json()['errcode']

    @allure.story("修改客服账号接口用例")
    @pytest.mark.parametrize('case', read_testCase("kf_mannage/update_kf.yaml"))
    def test_update(self, case, read_token):
        with allure.step("组装参数"):
            # token0 = read_token()
            # token0 = read_yamlFile("param/ac.yaml")
            # url = host + case['url'] + '?access_token=' + token0
            url = f"{host}{case['url']}?access_token={read_token}"
            param = case['data']
            logging.debug(f"------------param--{param}------------------")

        with allure.step("调用接口"):
            resp = requests_def(method=case['method'], url=url, json=param)
            resp.json()
            # assert_resp['statusCode']= resp.status_code
            logging.debug(f"--------修改--resp----{resp.json()}------------------")
            logging.debug(f"------修改----Expected----{case['excepted']}------------------")

        with allure.step("结果验证"):
            assert case["excepted"]['statusCode'] == resp.status_code
            assert case.get("excepted", {}).get("errcode") == resp.json()['errcode']

    @allure.story("删除客服账号接口用例")
    @pytest.mark.parametrize('case', read_testCase("kf_mannage/del_kf.yaml"))
    def test_del(self, case, read_token):
        with allure.step("组装参数"):
            url = f"{host}{case['url']}"
        with allure.step("调用接口"):
            resp = requests_def(method=case['method'], url=url,
                                params={
                                    "access_token": read_token,
                                    "kf_account": case['params']['kf_account']
                                })

            logging.debug(f"----------resp----{resp.json()}------------------")
            logging.debug(f"----------Expected----{case['excepted']}------------------")

        with allure.step("结果验证"):
            # assert case["excepted"]['statusCode'] == resp.status_code
            assert case.get("excepted", {}).get("errcode") == resp.json()['errcode'], "删除的返回errcode错误"
