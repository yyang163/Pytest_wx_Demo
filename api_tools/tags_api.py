import logging

from Config.config_init import read_config
from common.random_def import read_yaml, get_random_digits, generate_random_string
from common.requests_def import requests_def

host = read_config("env", "test")
select_tag_url = read_config("api", "select_tags_url")
# delect_tag_url = read_config("api", "delect_tags_url")
add_tag_url = read_config("api", "add_tags_url")


def select_tags():
    body = requests_def(method="get", url=host + select_tag_url,
                        params={'access_token': read_yaml("access_token.yaml")})

    tags = body.json()['tags']
    all_tag_id = [1, 2, 3]
    for i in range(len(tags)):
        all_tag_id.append(tags[i]["id"])
    i = get_random_digits(0, len(all_tag_id))
    ID = str(all_tag_id[int(i)])
    logging.info("调用查询用户标签接口，获取测试参数-接口相应结果" + str(body.json()))
    return ID


# def del_tags(del_id):
#     body = requests_def(method="post", url=host + delect_tag_url,
#                         params={"access_token": read_yaml('access_token.yaml')},
#                         json={"tags": {"id": del_id}})
#     logging.info("调用删除用户标签接口，获取测试参数-接口相应结果" + str(body.json()))
#
#     def add_tags():
#         body = requests_def(method="post", url=host + add_tag_url,
#                             params={"access_token": read_yaml('access_token.yaml')},
#                             json={"tags": {"name": generate_random_string(30)}})
#         ID = body.json()["tag"]['id']
#         return ID
