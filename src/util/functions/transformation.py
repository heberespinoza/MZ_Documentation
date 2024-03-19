import requests
import json
import math
import urllib
import datetime
from pandasql import sqldf
from collections import OrderedDict



def create_smaller_dict(dict_list, keys):
    smaller_dict = []
    for d in dict_list:
        if isinstance(d, dict):
            smaller_dict.append({key: d.get(key) for key in keys})
    return smaller_dict


def count_unique_values(dict_list, key):
    unique_values = set()
    for d in dict_list:
        if key in d and d[key] is not None:
            value = d[key]
            if isinstance(value, list):
                unique_values.update(value)
            else:
                unique_values.add(value)
    return len(unique_values)


def encode_key(keys):
    """Encodes a list of keys for use in a URL."""
    encoded_keys = []
    for key in keys:
        key = key.strip("'\"")
        encoded_key = urllib.parse.quote_plus(key)
        encoded_keys.append(encoded_key)
    return encoded_keys


def to_url(endpoint, keys):
    results = []
    for key in keys:
        results.append(endpoint.format(key))
    return results


def join_dictionaries(dictionaries):
    if not dictionaries:
        return {}

    merged_dict = {}
    for dictionary in dictionaries:
        if dictionary is not None and isinstance(dictionary, dict):
            for key, value in dictionary.items():
                if key not in merged_dict:
                    merged_dict[key] = value
                else:
                    if isinstance(value, list):
                        merged_dict[key].extend(value)
                    else:
                        merged_dict[key] = value
        else:
            print("Warning: Non-dictionary element found in the input list.")

    return merged_dict


def extract_list_values(arr, index):
    return [sub_arr[index] for sub_arr in arr]


def format_sp_list(lst):
    def format_value(value):
        if isinstance(value, str) or isinstance(value, datetime.date):
            return f"'{value}'"
        return str(value)

    if len(lst) == 1:
        formatted_value = format_value(lst[0])
        return f"({formatted_value})"
    else:
        formatted_values = ', '.join(format_value(value) for value in lst)
        return f"({formatted_values})"

