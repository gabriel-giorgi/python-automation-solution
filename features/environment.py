from selenium import webdriver
import os

head, tail = os.path.split(os.path.dirname(os.path.abspath(__file__)))
CHROME_PATH = head + r"\drivers\chromedriver.exe"


def before_all(context):
    pass

def before_feature(context, feature):
    context.chrome_path = CHROME_PATH
    context.feature_name = feature.name


def before_scenario(context, scenario):
    # Receives context and scenario as parameter
    context.scenario_name = scenario.name
    context.driver = webdriver.Chrome(context.chrome_path)
    context.driver.maximize_window()


def after_scenario(context, scenario):
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
