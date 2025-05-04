import random
import string
import yaml
from Config.config_init import read_config

base_path = read_config("path", "Data_path")
param_path = read_config("path", "param_path")


def get_random_digits(min_number, max_number):
    return random.randint(int(min_number), int(max_number))


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    # random_string = ''.join(random.choice(characters) for _ in range(int(length)))
    random_string = ""
    for _ in range(length):
        this_char = random.choices(characters)
        random_string = random_string + this_char[0]
    return random_string


def read_yaml(yaml_name):
    with open(param_path + "/" + yaml_name, mode='r', encoding='utf-8') as f:
        value = yaml.safe_load(f)
        return value


def get_kf_account():
    join_str = "_@"
    star_str = "kf"
    end_str = generate_random_string(10)
    kf_account = star_str + join_str + end_str
    return kf_account

# print(generate_random_string(8))
