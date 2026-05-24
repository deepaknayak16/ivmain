
#Initilize the Appium driver
from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# Desired capabilities for the Windows application
desired_caps = {
    "platformName": "Windows",
    "deviceName": "WindowsPC",
    "app": "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App",  # Example: Windows Calculator
}
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)
# Initialize the Appium driver
driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
#Locate Element
# Locate an element (e.g., a button in the calculator)
button_element = driver.find_element_by_name("5")  # Example: Locate the "5" button
# Locate an element (e.g., the result display in the calculator)
result_element = driver.find_element_by_accessibility_id("CalculatorResults")
#Perform Mouse Action
# Initialize ActionChains
actions = ActionChains(driver)
# Perform a single click
actions.click(button_element).perform()
# Perform a double-click
actions.double_click(button_element).perform()
# Perform a right-click
actions.context_click(button_element).perform()
# Perform a hover (move to element)
actions.move_to_element(button_element).perform()

#Drag and Drop
# Locate source and target elements
source_element = driver.find_element_by_name("SourceElement")
target_element = driver.find_element_by_name("TargetElement")
# Perform drag and drop
actions.drag_and_drop(source_element, target_element).perform()
#Scroll (Mouse Wheel Actions)
#Use the scroll_to_element method or simulate mouse wheel actions.
# Scroll to an element
actions.move_to_element(button_element).perform()
#Release Actions
actions.release().perform()
#Perform Keyboard Actions
# Send text to an input field (if applicable)
result_element.send_keys("123")  # Example: Enter "123" into the calculator

# Send special keys (e.g., Enter, Tab, Backspace)
result_element.send_keys(Keys.ENTER)  # Press Enter
result_element.send_keys(Keys.TAB)    # Press Tab
result_element.send_keys(Keys.BACKSPACE)  # Press Backspace

#Key Combinations 
# Initialize ActionChains
actions = ActionChains(driver)
# Perform key combination (e.g., Ctrl+C)
actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
# Perform key combination (e.g., Ctrl+V)
actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

#Simulate Typing
# Simulate typing text
result_element.send_keys("Hello, World!")

#Clear Input Field
# Clear the input field
result_element.clear()

#Press ENTER Key Using Actions Class
# Initialize the Actions class
actions = ActionChains(driver)
# Press the ENTER key
actions.send_keys(Keys.ENTER).perform()

#SHIFT Key for Uppercase Letters
# Initialize the Actions class
actions = ActionChains(driver)
# Press SHIFT, type a letter, and release SHIFT
actions.key_down(Keys.SHIFT).send_keys("a").key_up(Keys.SHIFT).perform()