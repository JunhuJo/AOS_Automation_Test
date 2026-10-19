import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from Automation_Test_Method import AOS_Automation_Test


@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "R3CW60CVL3R"
    options.app_package = "com.qa.practiceapp"
    options.app_activity = ".LoginActivity"
    options.no_reset = False

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()

@pytest.fixture
def AOS_Driver(driver):
    return AOS_Automation_Test(driver)