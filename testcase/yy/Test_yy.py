import allure
import pytest

from api_tools.get_token import yy_fixture


def get_case_array():
    # 用例的数据源 可以读yaml文件/读excel文件/数据库
    return [
        {'a': 1, 'b': 2, 'c': 3, 'res': 9},
        {'a': 2, 'b': 2, 'c': 3, 'res': 12},
        {'a': 2, 'b': 3, 'c': 3, 'res': 15}
    ]


@allure.epic("杨杨项目")
@allure.feature('自测功能')
class Test_yy:

    # @pytest.mark.parametrize('args', [1, 2, 3])
    # @pytest.mark.parametrize('args', {'a': 1, 'b': 2, 'c': 3})
    @allure.story("自测加法用例")
    @pytest.mark.parametrize('case', get_case_array())
    def test_yyy(self, case, yy_fixture):
        # print(f'------------{case}------------')
        # 业务逻辑
        # 断言：判断 （a + b）* c 是否等于 res
        assert (case['a'] + case['b']) * case['c'] == case['res']

    @allure.story("自测2222用例")
    @pytest.mark.parametrize('case', get_case_array())
    def test_yy2(self, case):
        # print(f'------------{case}------------')
        # 业务逻辑
        # 断言：判断 （a + b）* c 是否等于 res
        assert (case['a'] + case['b']) * case['c'] == case['res']

    # def test_case():
    #     suc_count = 0
    #     fail_count = 0
    #     cases = [
    #         {'a': 1, 'b': 2, 'c': 3, 'res': 9},
    #         {'a': 8, 'b': 2, 'c': 3, 'res': 10},
    #         {'a': 2, 'b': 2, 'c': 3, 'res': 3}
    #     ]
    #     for case in cases:
    #         print(f"当前循环参数：{case}")
    #         if (case['a'] + case['b']) * case['c'] == case['res']:
    #             suc_count = suc_count + 1
    #         else:
    #             fail_count = fail_count + 1
    #     print(f"用例成功了{suc_count}条，失败了{fail_count}条")
