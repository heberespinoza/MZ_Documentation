import configparser
import os
import pymysql
from definitions import CONFIG_PATH


def get_config_data(section):
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    config_dict = dict(config.items(section))
    return config_dict


def mysql_connection():
    credentials_dict = get_config_data('MYSQL')
    connection_object = pymysql.connect(**credentials_dict)
    return connection_object


def get_mysql_query(query):
    conn = mysql_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    # Execute a SQL query
    results = cursor.execute(query)
    # Fetch the results
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results




# credentials_dict = get_config_data('MYSQL')
# print(credentials_dict)

