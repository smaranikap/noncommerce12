from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='Chrome':
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        print("Launching chrome browser")
    elif browser=='firefox':
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
        print("Launching firefox browser")
    else:
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


############## HTML Report ############

# it is hook for adding Environent info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'non Commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester Name'] = 'Smaranika'

# it is hook for delete/modify Environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('Java_home',None)
    metadata.pop('Plugins', None)





