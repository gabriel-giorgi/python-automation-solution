import sys
from selenium import webdriver
import os
import time
from utils.config_handler import get_property_file_value
head, tail = os.path.split(os.path.dirname(os.path.abspath(__file__)))
CHROME_PATH = head + r"\LFS\drivers\chromedriver.exe"


def before_all(context):
    pass

def before_feature(context, feature):
    sys.path.append(head)
    context.chrome_path = CHROME_PATH
    context.feature_name = feature.name
    context.redmine_url = get_property_file_value('URL')


def before_scenario(context, scenario):
    # Receives context and scenario as parameter
    context.scenario_name = scenario.name
    context.driver = webdriver.Chrome(context.chrome_path)
    context.driver.maximize_window()


def after_scenario(context, scenario):
    file_extension = ".png"
    path_passed_test = os.path.normpath(r'\reports\passed_tests') + "\\"
    path_failed_test = r'\reports\failed_tests\\'

    if context.failed:
        ts = time.gmtime()
        time_stamp = time.strftime("%Y-%m-%d %H-%M-%S", ts)
        screenshot_path = head + path_failed_test + scenario.name.lower().replace(" ", "_").split("-")[0] + time_stamp.replace(" ", "") + file_extension
        context.driver.save_screenshot(screenshot_path)
    else:
        ts = time.gmtime()
        time_stamp = time.strftime("%Y-%m-%d %H-%M-%S", ts)
        screenshot_path = head + path_passed_test + scenario.name.lower().replace(" ", "_").split("-")[0] + time_stamp.replace(" ", "") + file_extension
        context.driver.save_screenshot(screenshot_path)
    try:
        context.driver.quit()

    except Exception as e:
        print(
            4 * "<" + "[ERROR]" + 4 * ">" + "An error occurred in after_scenario() method: "
            + "\nERROR: "
            + format(e)
            + "\n")

def after_feature(context, feature):
    pass


def after_all(context):
    pass
