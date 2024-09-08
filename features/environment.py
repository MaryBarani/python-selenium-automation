from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from selenium.webdriver.edge.options import Options
from support.logger import logger


def browser_init(context):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)
    # context.driver = webdriver.Safari()

    # # BrowserStack configuration
    # BROWSERSTACK_CONFIG = {
    #     'bstack:options': {
    #         'os': 'Windows',
    #         'osVersion': '10',
    #         'resolution': '1920x1080',
    #         'sessionName': 'Internship_Project',
    #         'buildName': 'Internship_Project_Build',
    #         'userName': 'mary_bCHue6',
    #         'accessKey': 'UphCy53ptH9UisefSaqN',
    #     },
    #     'browserName': 'Chrome',
    #     'browserVersion': 'latest',
    # }
    #
    # # Initialize WebDriver with capabilities
    # options = webdriver.ChromeOptions()
    # options.set_capability('bstack:options', BROWSERSTACK_CONFIG['bstack:options'])
    # options.set_capability('browserName', BROWSERSTACK_CONFIG['browserName'])
    # options.set_capability('browserVersion', BROWSERSTACK_CONFIG['browserVersion'])
    #
    # context.driver = webdriver.Remote(
    #     command_executor='https://hub-cloud.browserstack.com/wd/hub',
    #     options=options
    # )
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context)


def before_step(context, step):
    logger.info(f'\nStarted step: {step}')
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'\nStep failed: {step}')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()


