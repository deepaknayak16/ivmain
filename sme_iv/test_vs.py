 

# from math import log10
# def rev(num):
#     def rec(num, tens):
#         if num < 10:
#             return num        
#         else:
#             return num % 10 * tens + rec(num // 10, tens // 10)
#     return rec(num, 10 ** int(log10(num)))
# print(rev(9901))





# ## Find Alphabet from a List 
# import string
# list = ['h', 'e', 'l', '5', 'o']
# newlist = []
# newdigit = []
# d={"letter":0 , "digit":0}
# for c in list:
#     if c.isalpha():
#         newlist+=c
#         d["letter"]+=1
#     elif c.isdigit():
#         newdigit+=c
#         d["digit"]+=1
#     else:
#         pass
# print ("letter", d["letter"])
# print ("digit", d["digit"])
# print (newlist)
# print (newdigit)





# d={}
# d['deepak'] = 0
# d['nayak'] = 0 
# f = [ '1, deepak, 15',
# '2, nayak, 10',
#  '3, deepak, 10',
#  '4, nayak, 13',
#  '3, deepak, 11',
#  '4, nayak, 15',
#  '3, deepak, 12',
#  '4, nayak, 14']
# for lines in f:
#     print(lines)
#     ##appropriate logic to excute#
#     line = lines.split(', ')
#     d[line[1]] += int(line[-1])
# print(d)






# # object destoryer 
# class Test:
#     def __del__(self):
#         print ("deleted")
#         test = Test()
#         del test



# #Find the second most repeated word in a given string
# def word_count(str):
#     counts = dict()
#     words = str.split()

#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1

#     counts_x = sorted(counts.items(), key=lambda kv: kv[1])
#     print(counts_x)
#     return counts_x[-1]
 
# print(word_count("deepy dipu deepy deepy "))

# #Find the first repeated word in a given string
# def first_repeated_word(str1):
#   temp = set()
#   for word in str1.split():
#     if word in temp:
#       return word
#     else:
#       temp.add(word)
#   return 'None'
# print(first_repeated_word("ab ca bc ab "))
# print(first_repeated_word("ab ca bc ab ca ab bc"))
# print(first_repeated_word("ab ca bc ca ab bc"))
# print(first_repeated_word("ab ca bc"))



# def no_of_substring_with_equalEnds(str1): 
# 	result = 0; 
# 	n = len(str1); 
# 	for i in range(n): 
# 		for j in range(i, n): 
# 			if (str1[i] == str1[j]): 
# 				result = result + 1
# 	return result 
# str1 = input("Input a string: ")
# print(no_of_substring_with_equalEnds(str1))



# def reverse_string_words(text):
#     for line in text.split('\n'):
#         return(' '.join(line.split()[::-1]))
# print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
# print(reverse_string_words("Python Exercises."))




# x = 22
# print("\nOriginal Number: ", x)
# print("Left aligned (width 10)   :"+"{:< 10d}".format(x));
# print("Right aligned (width 10)  :"+"{:10d}".format(x));
# print("Center aligned (width 10) :"+"{:^10d}".format(x));
# print()


# with open("C:/Users/DIPPU/Documents/test.txt") as f:
#     with open("C:/Users/DIPPU/Documents/out.txt", "w") as f1:
#         for line in f:
#             f1.write(line)



# with open('C:/Users/DIPPU/Documents/test.txt') as fh1, open('C:/Users/DIPPU/Documents/out.txt') as fh2:
#     for line1, line2 in zip(fh1, fh2):
#         # line1 from abc.txt, line2 from test.txtg
#         print(line1)
#         print(line2)
#         print(line1+line2)


# def file_lengthy(fname):
#     with open(fname) as fh1:
#         for i, l in enumerate(fh1):
#             pass
#         return i + 1
# print("Number of lines in the file: ",file_lengthy("C:/Users/DIPPU/Documents/test.txt"))



# def longest_word(filename):
#     with open(filename, 'r') as infile:
#               words = infile.read().split()
#     max_len = len(max(words, key=len))




#     return [word for word in words if len(word) == max_len]

# print(longest_word('C:/Users/DIPPU/Documents/test.txt'))





# my_dict = dict.fromkeys(['a', 'b', 'c'], 10)
# my_dict.update(dict.fromkeys(['d', 'e'], 20))
# print (my_dict)
# #my_dict = {('a', 'c', 'd'): 10, ('b', 'e'): 20}
# next(v for k, v in my_dict.items() if 'b' in k)

# #How to print 'neduitn' using a single line of code from Days ?
days = "Mon Tue Wed Thu Fri Sat Sun"
re = days.split()
temp = ""
for day in re:
    temp = temp + (day[-1])
print (temp)
print (len(days))
import re
print(''.join(re.findall("(?i)[a-z](?!\\S)", days)))

# 1.	Write a program to find the length of the string "refrigerator" without using len function.
lene = sum(map(lambda x:1, "refrigerator"))
print(lene)

#2.	Write a program to find the first and the last occurrence of the letter 'o' and character ',' in "Hello, World".

def findLastIndex(str, x): 
    index = -1
    for i in range(0, len(str)): 
        if str[i] == x: 
            index = i 
    return index 
  # String in which char is to be found 
str = "geeksforgeeks"
# char whose index is to be found 
x = 'e' 
index = findLastIndex(str, x) 
if index == -1: 
    print("Character not found") 
else: 
    print('Last index is', index)

#Write a program to print every character of a string entered by user in a new line using loop.
a = 'googleindia'
for i in a:
  print (i)

#Write a program to check if the letter 'e' is present in the word 'Umbrella'.
print ('e' in 'Umbrella')

a = "This is orange juice"
print('orange' in a.split())
#the output should be R.B.Roser.
a = "Robert Brett Roser"
a = a.split()
b = a[0][0]+". "+a[1][0]+". "+a[2]
print (b)


from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
parent_window = driver.current_window_handle
# Open new window/tab (example action)
driver.execute_script("window.open('https://google.com')")
all_windows = driver.window_handles
# Switch to new window
for window in all_windows:
    if window != parent_window:
        driver.switch_to.window(window)
# Perform actions in new window
print(driver.title)
# Switch back
driver.switch_to.window(parent_window)


# All windows
all_windows = driver.window_handles
# Current window
parent = driver.current_window_handle
# Switch
for win in all_windows:
    if win != parent:
        driver.switch_to.window(win)



driver.switch_to.default_content()

driver.get("https://example.com")
driver.get("https://google.com")

driver.back()      # goes to example.com
driver.forward()   # goes to google.com
driver.refresh()   # refreshes google.com

driver.refresh()
driver.get(driver.current_url)
from selenium.webdriver.common.keys import Keys
driver.find_element("tag name", "body").send_keys(Keys.F5)


driver = webdriver.Chrome()
driver.get("https://example.com")
driver.maximize_window()            # maximize
driver.minimize_window()            # minimize
driver.set_window_size(1024, 768)   # Set Custom Window Size
driver.fullscreen_window()          # Full screen mode

element = driver.find_element("id", "message")
print(element.text)

element = driver.find_element("id", "username")
name = element.get_attribute("name")
class_name = element.get_attribute("class")
value = element.get_attribute("value")
print(name, class_name, value)

driver.delete_all_cookies()         # Removes all cookies from the browser
driver.delete_cookie("cookieName")  # Delete Specific Cookie by its name



driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://example.com")
driver.find_element("id", "username")  # waits up to 10 seconds

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.ID, "username")))


from selenium.webdriver.support import expected_conditions as EC
EC.visibility_of_element_located((By.ID, "username"))       # Wait until element is present and visible on page
EC.element_to_be_clickable((By.ID, "loginBtn"))             # Wait until element is clickable:
EC.presence_of_element_located((By.ID, "username"))         # Wait until element exists in HTML (may not be visible)
EC.title_contains("Google")                                 # Title contains text
EC.title_is("Google")                                       # Title is exact match
EC.alert_is_present()                                       # Wait for alert popup:
EC.text_to_be_present_in_element((By.ID, "msg"), "Success") # Wait until element contains specific text
EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1"))# Wait and switch to frame
EC.element_to_be_selected((By.ID, "checkBox"))              # Element selected For checkboxes or radio buttons
EC.visibility_of_all_elements_located((By.CLASS_NAME, "items")) #Wait for multiple elements:

#Fluent Wait Setup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=2,
    ignored_exceptions=[NoSuchElementException]
)
#Using Fluent Wait with Expected Condition
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

element = wait.until(
    EC.visibility_of_element_located((By.ID, "username")))


#1. Basic Keyboard Input
from selenium.webdriver.common.keys import Keys
element.send_keys("Hello") # Send text to an element
#2. Common Keyboard Operations
element.send_keys(Keys.ENTER) #Enter key
element.send_keys(Keys.TAB) # Tab key (move to next field)
element.send_keys(Keys.BACKSPACE) # Backspace (delete characters)
element.send_keys(Keys.DELETE) # Delete key
#3. Navigation Keys Arrow keys
element.send_keys(Keys.ARROW_UP)
element.send_keys(Keys.ARROW_DOWN)
element.send_keys(Keys.ARROW_LEFT)
element.send_keys(Keys.ARROW_RIGHT)
#4. Control Keys (Shortcuts)
element.send_keys(Keys.CONTROL, "a") #Select All (Ctrl + A)
element.send_keys(Keys.CONTROL, "c") #Copy (Ctrl + C)

#5. Special Keys Example
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

actions = ActionChains(driver)
actions.send_keys("Hello").perform()
#6. key_down() (Press Key) Used to press and hold a key.
actions.key_down(Keys.CONTROL).perform()
# 7. key_up() (Release Key) Used to release a held key.
actions.key_up(Keys.CONTROL).perform()
#Real Time Example
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL)\
       .send_keys("a")\
       .key_up(Keys.CONTROL)\
       .perform()


# 1. Click :: Performs a single left click
actions.click(element).perform()
#2. Double Click :: Performs a double click on an element
actions.double_click(element).perform()
#3. Right Click (Context Click) :: Opens context menu (right-click)
actions.context_click(element).perform()
#4. Mouse Hover (Move to Element) :: Moves mouse over an element (used for dropdowns/menus)
actions.move_to_element(element).perform()
#5. Drag and Drop :: Drags an element and drops it to another location
actions.drag_and_drop(source, target).perform()
#6. Click and Hold :: Clicks and holds the mouse button
actions.click_and_hold(element).perform()
#7. Release Mouse :: Releases the held mouse button
actions.release(element).perform()
#8. Move by Offset ::  Moves mouse by specific x, y coordinates
actions.move_by_offset(100, 50).perform()


current_url = driver.current_url
print(current_url)

driver.get("https://example.com")
print(driver.title)

html_source = driver.page_source
print(html_source)

element = driver.find_element(By.ID, "tooltip_element")
tooltip_text = element.get_attribute("title")
assert tooltip_text == "Expected tooltip text"

link = driver.find_element(By.LINK_TEXT, "Click Here")
link.click()
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Click")
link.click()


from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
caps = DesiredCapabilities.CHROME.copy()
caps["acceptInsecureCerts"] = True
driver = webdriver.Chrome(desired_capabilities=caps)
driver.get("https://example.com")
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.CHROME.copy()
caps["acceptInsecureCerts"] = True

driver = webdriver.Chrome(desired_capabilities=caps)
driver.get("https://example.com")

driver.quit()

links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print(link.text, "->", link.get_attribute("href"))



#1. Capture full page screenshot
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
driver.save_screenshot("page.png")
driver.quit()
#2. Capture screenshot using get_screenshot_as_file
driver.get_screenshot_as_file("page.png")
#3. Capture screenshot of a specific element
from selenium.webdriver.common.by import By
element = driver.find_element(By.ID, "logo")
element.screenshot("element.png")


from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get("https://example.com")
dropdown = Select(driver.find_element(By.ID, "dropdown_id"))
# Select by visible text
dropdown.select_by_visible_text("Option 1")
# Select by value
dropdown.select_by_value("1")
# Select by index
dropdown.select_by_index(0)

driver = webdriver.Chrome()
driver.get("https://example.com")
element = driver.find_element(By.ID, "element_id")
if element.is_displayed():
    print("Element is visible on the page")
else:
    print("Element is NOT visible")


driver = webdriver.Chrome()
driver.get("https://example.com")
element = driver.find_element(By.ID, "element_id")
if element.is_enabled():
    print("Element is enabled for interaction")
else:
    print("Element is disabled")
#dyanmic 
from selenium.webdriver.common.by import By
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "element_id")))
element.click()
driver = webdriver.Chrome()
driver.get("https://example.com")
alert = driver.switch_to.alert
print(alert.text)
alert.accept()   # OK
# alert.dismiss()  # Cancel

driver = webdriver.Chrome()
driver.get("https://example.com/upload")
file_input = driver.find_element(By.ID, "file-upload")
file_input.send_keys(r"C:\Users\YourName\Desktop\file.txt")