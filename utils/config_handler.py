import configparser
import os

head, tail = os.path.split(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = head + r'\config\config.txt'

def get_property_file_value(key):
    config_parser = configparser.RawConfigParser()
    config_file_path = CONFIG_PATH
    config_parser.read(config_file_path)
    value = config_parser.get('config', key)
    return value
