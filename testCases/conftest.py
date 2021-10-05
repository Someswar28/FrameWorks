import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--start-maximized")
        chrome_option.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(executable_path="C:\\Users\\hp\\OneDrive\\Desktop\\Selenium jars\\"
                                                  "chromeDriver\\chromedriver.exe", options=chrome_option)
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:\\Users\\hp\\OneDrive\\Desktop\\Selenium jars\\FF\\geckodriver.exe")

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['Project Name'] = 'non Commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester']= 'Someswar rao'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)