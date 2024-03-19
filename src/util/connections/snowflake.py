import configparser
import os
# import snowflake.connector
# from snowflake.connector import DictCursor
from snowflake.snowpark import Session
from src.util.functions.snowpark import CustomSession
from definitions import CONFIG_PATH


def get_config_data(section):
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    config_dict = dict(config.items(section))
    return config_dict


def snowpark_session():
    credentials_dict = get_config_data('SNOWPARK')
    session = Session.builder.configs(credentials_dict).create()
    return session


def snowpark_custom_session():
    session = snowpark_session()
    custom_session = CustomSession(session)
    return custom_session


def snowflake_connector(cursor_type):
    connection_dict = get_config_data('CONNECTOR')
    connection = snowflake.connector.connect(**connection_dict)
    dict_cursor = connection.cursor(DictCursor)
    cursor = connection.cursor()
    if cursor_type == 'DictCursor':
        return dict_cursor
    elif cursor_type == 'cursor':
        return cursor
    else:
        return print("Error: only available options are: DictCursor, cursor")










