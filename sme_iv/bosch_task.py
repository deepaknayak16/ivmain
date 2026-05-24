


import unittest
"""
This module contains automated tests for a Windows application using Appium and unittest framework.
Classes:
    FieldButtonTests: A unittest.TestCase subclass that contains tests for field and button interactions.
Functions:
    generate_options: Generates different sets of WindowsOptions for Appium.
    driver: A pytest fixture that initializes and quits the Appium driver.
    test_app_source_could_be_retrieved: A test function that asserts the app source can be retrieved.
Locators:
    MobileBy: Provides a set of locator strategies that can be used with Appium.
"""
from appium import webdriver

class FieldButtonTests(unittest.TestCase):

    @classmethod

    def setUpClass(self): 
    
        desired_caps = {                    
                        'platformName': 'Windows',
                        'deviceName': 'WindowsPC'
                        }
        desired_caps["app"] = ""
        # Start Appium session
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities= desired_caps)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_initialize(self):
        self.driver.find_element_by_name("Save").click()
        self.driver.find_element_by_name("Clear").click()

    def test_field(self):
        input_field_locator = (self.driver.find_element_by_name, 'textfiled')
        # Find the input field and enter text
        input_field = self.driver.find_element(*input_field_locator)
        input_field.send_keys('MyTestInput')

        if input_field.is_enabled():
            print("Test case passed: input_field is enabled after entering input.")
        else:
            print("Test case failed: input_field is not enabled after entering input.")

    def test_buttion(self):
        submit_button_locator = (self.driver.find_element_by_name, 'SubmitButton')

        submit_button = self.driver.find_element(*submit_button_locator)

        if submit_button.is_enabled():
            print("Test case passed: Submit button is enabled after entering input.")
        else:
            print("Test case failed: Submit button is not enabled after entering input.")

if __name__ == '__main__':
    unittest.TestLoader().TestCase(FieldButtonTests).run()


import pytest

from appium import webdriver
# Options are available in Python client since v2.6.0
from appium.options.windows import WindowsOptions

def generate_options():
    uwp_options = WindowsOptions()
    # How to get the app ID for Universal Windows Apps (UWP):
    # https://www.securitylearningacademy.com/mod/book/view.php?id=13829&chapterid=678
    uwp_options.app = 'Microsoft.WindowsCalculator_8wekyb3d8bbwe!App'

    classic_options = WindowsOptions()
    classic_options.app = 'C:\\Windows\\System32\\notepad.exe'
    # Make sure arguments are quoted/escaped properly if necessary:
    # https://ss64.com/nt/syntax-esc.html
    classic_options.app_arguments = 'D:\\log.txt'
    classic_options.app_working_dir = 'D:\\'

    use_existing_app_options = WindowsOptions()
    # Active window handles could be retrieved from any compatible UI inspector app:
    # https://docs.microsoft.com/en-us/windows/win32/winauto/inspect-objects
    # or https://accessibilityinsights.io/.
    # Also, it is possible to use the corresponding WinApi calls for this purpose:
    # https://referencesource.microsoft.com/#System/services/monitoring/system/diagnosticts/ProcessManager.cs,db7ac68b7cb40db1
    #
    # This capability could be used to create a workaround for UWP apps startup:
    # https://github.com/microsoft/WinAppDriver/blob/master/Samples/C%23/StickyNotesTest/StickyNotesSession.cs
    use_existing_app_options.app_top_level_window = hex(12345)

    return [uwp_options, classic_options, use_existing_app_options]


@pytest.fixture(params=generate_options())
def driver(request):
    # The default URL is http://127.0.0.1:4723/wd/hub in Appium 1
    drv = webdriver.Remote('http://127.0.0.1:4723', options=request.param)
    yield drv
    drv.quit()


def test_app_source_could_be_retrieved(driver):
    assert len(driver.page_source) > 0

'''
type of locator used in appium
'''
from appium.webdriver.common.mobileby import MobileBy

# Find element by accessibility id
element = driver.find_element(MobileBy.ACCESSIBILITY_ID, 'someAccessibilityId')
# Find element by class name
element = driver.find_element(MobileBy.CLASS_NAME, 'some    ClassName')
# Find element by id
element = driver.find_element(MobileBy.ID, 'someId')
# Find element by name
element = driver.find_element(MobileBy.NAME, 'someName')
# Find element by xpath
element = driver.find_element(MobileBy.XPATH, 'someXpath')
# Find element by image
element = driver.find_element(MobileBy.IMAGE, 'someImage')
# Find element by custom
element = driver.find_element(MobileBy.CUSTOM, 'someCustom')

# Desired Capabilities
desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "/path/to/app.apk",
    "automationName": "UiAutomator2"
}

# Initialize driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# Find element by ID and click
login_button = driver.find_element(By.ID, "com.example.app:id/login_button")
login_button.click()

# Find element by Accessibility ID and type text
username_field = driver.find_element(By.ACCESSIBILITY_ID, "username_field")
username_field.send_keys("testuser")

# Close the session
driver.quit()