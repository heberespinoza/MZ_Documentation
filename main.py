import configparser
import os
from snowflake.snowpark import Session
from definitions import CONFIG_PATH

config = configparser.ConfigParser()
config.read(CONFIG_PATH)
print(config)
print(type(config))


print(type(config.items('SNOWFLAKE')))
#for sect in config.sections():
    #config_dict[sect] = dict(config.items(sect))


d=dict(config.items('SNOWFLAKE'))
print(d)