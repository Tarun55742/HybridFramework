from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
    elif browser=='firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#######  Pytest HTML Reports   #######

# # It is hook for adding environment info to HTMl
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Orange HRM'
#     config._metadata['Module Name'] = 'Admin'
#     config._metadata['Tester'] = 'Tarun'
#
# # # It is hook for Delete/Modify environment info to HTMl
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)





