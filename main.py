import os

import pytest

from api_tools.get_token import get_token

if __name__ == '__main__':
    get_token()
    # write_yaml("ac.yaml", get_token()["access_token"])
    # 执行单个文件 指定文件名
    # pytest.main([__file__, '-vs', 'testcase/kt/Test_kt.py'])
    # pytest.main([__file__, '-vs', 'testcase/kt/Test_kt1.py', 'testcase/kt/Test_kt2.py'])
    # 执行全部用例 根据配置文件pytest.ini中的testpaths、python_files、python_classes、python_functions来决定
    pytest.main()
    # allure将生成的报告由json格式（pytest通过命令--alluredir指定）转换成h5格式 写入报告之前先清除
    os.system('allure generate ./temp_JsonReport -o ./report --clean')
    # allure自动打开报告
    os.system('allure open ./report')
