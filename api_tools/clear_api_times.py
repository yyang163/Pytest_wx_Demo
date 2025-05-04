from Config.config_init import read_config
from common.random_def import read_yaml
from common.requests_def import requests_def

host = read_config("env", "test")
appid = read_config("env", "appid")


def clear_api_times():
    body = requests_def(method="post", url=host + "/cgi-bin/clear_quota",
                        params={'access_token': read_yaml("access_token")}, json={"appid", appid})
    return body.json()


print(clear_api_times())
