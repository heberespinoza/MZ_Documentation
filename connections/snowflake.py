import configparser
import os
from snowflake.snowpark import Session
from definitions import CONFIG_PATH


def get_config_data(section):
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    config_dict = dict(config.items(section))
    return config_dict


def snowpark_session():
    connection_parameters = get_config_data('SNOWPARK')
    session = Session.builder.configs(connection_parameters).create()
    return session




