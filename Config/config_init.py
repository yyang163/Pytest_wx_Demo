'''
import configparser


filename=r"config/config.ini"
inifile = configparser.ConfigParser()
inifile.read(filename, encoding="UTF-8")
print(inifile.get("env","test"))
'''

'''
import configparser

path = r"config/config.ini"
file = configparser.ConfigParser()
file.read(path, encoding="utf-8")


print(file.get("path", "OpenReport_path"))
'''
import configparser


def read_config(section, key):
    path = r"Config/config.ini"
    conf = configparser.ConfigParser()
    conf.read(path, encoding="utf-8")
    value = conf.get(section, key)
    return value


print(read_config("path", "OpenReport_path"))


def read_config(section, key):
    path = r"Config/config.ini"
    conf = configparser.ConfigParser()
    conf.read(path, encoding="utf-8")
    value = conf.get(section, key)
    return value

# print(read_config("path", "OpenReport_path"))
