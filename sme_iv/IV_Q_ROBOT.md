robot-framework-project/
│
├── tests/                          # Only test execution layer
│   ├── ui/
│   │   ├── login/
│   │   │   ├── test_login.robot
│   │   │   └── test_login_negative.robot
│   │   └── dashboard/
│   │       └── test_dashboard.robot
│   │
│   └── api/
│       └── test_user_api.robot
│
├── resources/                      # Reusable layer (core framework)
│   ├── keywords/
│   │   ├── common_keywords.robot
│   │   └── login_keywords.robot
│   │
│   ├── pages/                      # POM layer (VERY IMPORTANT)
│   │   └── login_page.robot
│   │
│   ├── locators/
│   │   └── login_locators.robot
│   │
│   ├── variables/
│   │   └── common_variables.robot
│   │
│   └── utils/
│       └── helpers.robot
│
├── libraries/                      # Python custom libraries
│   └── custom_library.py
│
├── configs/                        # Environment configs
│   ├── qa.py
│   ├── stage.py
│   └── prod.py
│
├── data/                           # Test data
│   ├── test_data.xlsx
│   └── test_data.json
│
├── results/                        # Auto-generated reports
│   ├── log.html
│   ├── report.html
│   └── output.xml
│
├── logs/                           # Framework logs
│   ├── execution.log
│   └── error.log
│
├── scripts/                        # Execution helpers
│   ├── run_tests.sh
│   └── run_tests.bat
│
├── requirements.txt
├── README.md
└── .gitignore

1. Config File (config.robot)
*** Variables ***     #### variables in Robot Framework
${BROWSER}      chrome
${BASE_URL}     https://example.com/login
${TIMEOUT}      10s 

*** Settings ***

Library    SeleniumLibrary

*** Variables ***
${USERNAME_FIELD}    id=username
${PASSWORD_FIELD}    id=password
${LOGIN_BUTTON}      id=loginBtn
${ERROR_MSG}         xpath=//div[@class='error']
${DASHBOARD_TEXT}    Dashboard

*** Keywords ***    ###  pass arguments to a user-defined keyword ###

Enter Username
    [Arguments]    ${username}
    Input Text    ${USERNAME_FIELD}    ${username}

Enter Password
    [Arguments]    ${password}
    Input Password    ${PASSWORD_FIELD}    ${password}

Click Login
    Click Button    ${LOGIN_BUTTON}

Verify Login Success
    Page Should Contain    ${DASHBOARD_TEXT}

Verify Login Failure
    Page Should Contain Element    ${ERROR_MSG}

3. Common Keywords (keywords.robot)
*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/config.robot    #### resource file in Robot Framework  ####  import a resource file

*** Keywords ***    ### create a user-defined keyword ###

Open Browser To App
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Timeout    ${TIMEOUT}

Close Browser Session
    Close Browser


4. Test Case (test_login.robot)
*** Settings ***
Library     SeleniumLibrary
Resource    ../resources/keywords.robot
Resource    ../pages/login_page.robot

Suite Setup       Open Browser To App
Suite Teardown    Close Browser Session

*** Test Cases ***

Valid Login Test
    Enter Username    testuser
    Enter Password    testpass
    Click Login
    Verify Login Success

Invalid Login Test
    Enter Username    wronguser
    Enter Password    wrongpass
    Click Login
    Verify Login Failure

5. Reporting (Built-in + Advanced)
    Robot Framework automatically generates:
        report.html
        log.html
        output.xml
    robot -d reports tests/
6. Environment File env.yaml

    url: https://example.com/login
    browser: chrome
    username: testuser
    password: testpass
    timeout: 10s
    dashboard_text: Dashboard
    error_msg: Dashboard


Use in Robot:
    Library    OperatingSystem
    Library    Collections

7. Run Script (run_tests.bat)
@echo off
robot -d reports tests/
pause

## ADD Two Numbers
1. *** Test Cases ***
    Add Two Numbers
        ${a}=    Set Variable    10
        ${b}=    Set Variable    20
        ${sum}=  Evaluate    ${a} + ${b}
        Log To Console    Sum is: ${sum}
        
2.  *** Using Python Library ***
    You can also create a Python file:
    # math_utils.py
        def add(a, b):
            return a + b
    
    Use in Robot:
        *** Settings ***   ##### import a library in Robot Framework
        
        Library    math_utils.py
        
        *** Test Cases ***
        Addition Using Python
                ${res}=    Add    10    15
                Log To Console    ${res}

## Question
1. How do you run a Robot Framework test case?

    Use the `robot` command:
        ```
        robot -d reports tests/test_login.robot
        ```
2. What is the difference between a test case and a keyword?

    A Test Case is a complete test scenario that validates a specific functionality (end-to-end or partial flow).  Test Cases → Business logic

    A Keyword is a reusable function (step or group of steps) used inside test cases to perform actions.    Keywords → Technical implementation (POM layer)

3. What are scalar, list, and dictionary variables in Robot Framework? 
    Scalar variables store a single value (${VAR}), 
        
        *** Variables ***
        ${USERNAME}    admin
        ${COUNT}       10

        # Acess Them
        Log    ${USERNAME}

    list variables store multiple values (@{LIST}), 
        
        *** Variables ***
        @{FRUITS}    apple    banana    mango
        
        # Acess Them 
        Log    ${FRUITS}[0]    # apple
        FOR    ${item}    IN    @{FRUITS}
            Log    ${item}
        END
        
    dictionary variables store key-value pairs (&{DICT})

          ***Variables ***
        &{USER}    name=admin    password=1234

        #Access Them
        Log    ${USER}['name']      OR  Log    ${USER.name}
        Log    ${USER}['password']  OR  Log    ${USER.password}
    These help in handling dynamic test data efficiently, especially in data-driven testing and reusable keyword design.  

4.  What is a Test Case Tag in Robot Framework?
    A test case tag is a label assigned to a test case to categorize, organize, and control execution of tests.
        Why Tags are Used
            Group test cases (e.g., smoke, regression)
            Run specific sets of tests
            Exclude unwanted tests
            Improve reporting and filtering
        
        *** Test Cases ***
        Valid Login Test
            [Tags]    smoke    login    regression
            Log    Login successful

        Invalid Login Test
            [Tags]    negative    login
            Log    Login failed

        Run only smoke tests:
            robot -i smoke tests/

        Exclude regression tests:
            robot -e regression tests/

5. How do you execute a specific test case within a test suite?
    Use the `--test` option with the `robot` command:
        ```
        robot --test "Valid Login Test" tests/web_tests/login_tests.robot
        ```

6.   How do you execute a specific test suite within a directory?
    Use the `--suite` option with the `robot` command:
        ```
        robot --suite suite_name path/to/tests
        ```

7.  What is the purpose of the `*** Documentation ***` section?
        The `*** Documentation ***` section is used to provide descriptive documentation for
        the test suite, test case, or keyword.

8.  How do you execute tests in parallel using Robot Framework?
        Use the Pabot library to execute tests in parallel:
        1.  Install Pabot
                pip install robotframework-pabot
        2.  Run Tests in Parallel
                robot -pabot --processes 4 tests/
                        processes 4 → runs 4 tests simultaneously
                        Each process uses a separate browser/session
                    Example
                        robot -pabot --processes 3 --outputdir reports tests/
        3.  Run specific tests with tags
                pabot -i smoke --processes 2 tests/

9.  How to Handle Errors in Robot Framework
        Robot Framework provides multiple ways to handle, control, and recover from errors during test execution.
        1. Run Keyword And Ignore Error
            Executes a keyword and does not fail the test immediately
                *** Test Cases ***
                    Handle Error Example
                    ${status}    ${result}=    Run Keyword And Ignore Error    Click Element    id=login
                    Log    Status: ${status}

        2. Run Keyword And Continue On Failure
            Test continues even if the step fails and Failure is still recorded
                Run Keyword And Continue On Failure    Click Element    id=wrong

        3. Run Keyword And Expect Error : >>>> Used for negative testing
                Run Keyword And Expect Error    *not found*    Click Element    id=invalid

        4. TRY / EXCEPT 
                *** Test Cases ***
                Try Catch Example
                    TRY
                        Click Element    id=login
                    EXCEPT
                        Log    Element not found
                    END

        5. Test Setup / Teardown Handling
                *** Settings ***
                Test Teardown    Run Keyword If Test Failed    Capture Page Screenshot

        6. Custom Error Handling Keyword
                *** Keywords ***
                Safe Click
                    [Arguments]    ${locator}
                    TRY
                        Click Element    ${locator}
                    EXCEPT
                        Log    Failed to click ${locator}
                    END
        7. Timeout & Wait Handling (Real Issue Fix)
                Wait Until Element Is Visible    id=login    10s

10. How do you `handle` and ` manage test dependencies` setup and teardown in Robot Framework?
        Setup → Runs before a test (or suite) to prepare the environment
        Teardown → Runs after a test (or suite) for cleanup, even if the test fails
        1. Test-Level Setup & Teardown
                *** Settings ***
                Test Setup       Open Browser To App
                Test Teardown    Close Browser

                *** Test Cases ***
                Login Test
                    Input Username    admin
                    Input Password    admin123
                    Click Login

        2. Suite-Level Setup & Teardown
                *** Settings ***
                Suite Setup       Open Browser To App
                Suite Teardown    Close Browser
                
        3.  Conditional Teardown (Very Important)
                *** Settings ***
                Test Teardown    Run Keyword If Test Failed    Capture Page Screenshot

11. How do you pass environment variables to Robot Framework?
        1. Using Command Line (--variable) ⭐ Most Common
            robot --variable URL:https://qa.example.com --variable BROWSER:chrome tests/
            Use in Robot
                ** Variables ***
                ${URL}
        2. Using Variable Files (Python / YAML)
                Python file (env.py)
                    URL = "https://qa.example.com"
                    BROWSER = "chrome"
                Run:
                    robot --variablefile env.py tests/
                YAML file (env.yaml) (with plugin)
                        URL: https://qa.example.com
                        BROWSER: chrome
                Run:
                    robot --variablefile env.yaml tests/

12. What is the purpose of the `*** Metadata ***` section?
        The `*** Metadata ***` section is used to define metadata for the test suite, such as
        version information or author details

13. How do you handle conditional execution in Robot Framework?
        Use the `Run Keyword If` keyword for conditional execution:
            *** Keywords ***
            Run Keyword If '${condition}' == 'value' Keyword To Run
            *** Multi Condotion ***
            Run Keyword If '${condition1}' == 'value1' and '${condition2}' == 'value2' Keyword To Run

14. How do you run keywords conditionally based on the outcome of previous keywords?
        Use the `Run Keyword If` keyword with a conditional expression:
            *** Keywords ***
            Run Keyword If '${status}' == 'PASS' Keyword To Run
        Use of the `Run Keywords` allows you to run multiple keywords in a sequence.
            *** Multi Keyword ***  
            Run Keywords Keyword 1 AND Keyword 2 AND Keyword 3


15.  How do you skip a test case in Robot Framework?
        Use the `Skip` keyword to skip a test case:
            `Skip Skipping this test case`

16. How do you run a keyword with a timeout in Robot Framework?
        Use the `Run Keyword With Timeout` keyword to specify a timeout for the keyword:
            `Run Keyword With Timeout 10s Keyword To Run`

17. How do you wait for a keyword to complete in Robot Framework?
        Use the `Wait Until Keyword Succeeds` keyword to wait for the keyword to complete:
            `Wait Until Keyword Succeeds 10s 1s Keyword To Wait For`

18. How do you run a keyword and return its result in Robot Framework?
        Use the `Run Keyword And Return` keyword to run the keyword and return its result:
            `${result} Run Keyword And Return Keyword To Run`

19.  How do you run a keyword and return its status and output in Robot Framework?
        Use the `Run Keyword And Return Status And Output` keyword to run the keyword and return its status and output:
            `${status} ${output} Run Keyword And Return Status And Output Keyword To Run`

20. How do you run a keyword for each item in a list with a specific index in Robot Framework?
        Use the `FOR` loop with index to run the keyword for each item in a list:
        ``` 
        FOR ${index} ${item} IN ENUMERATE @{LIST}
            Keyword To Run ${index} ${item}
        END
        ```

21. How do you run a keyword with arguments and store the result in Robot Framework?
        Use the `Run Keyword And Return` keyword with arguments and store the result:
            `${result} Run Keyword And Return Keyword To Run arg1 arg2`

22. What are the built-in libraries in Robot Framework?
        - BuiltIn == `Log`, `Sleep`, and `Set Variable`
        - Collections
        - DateTime
        - Dialogs
        - OperatingSystem
        - Process
        - Screenshot
        - String
        - Telnet
        - XML
        

23. What is the difference between `Run Keyword And Continue On Failure` and `Run Keyword And Ignore Error`?
        `Run Keyword And Continue On Failure` runs the keyword and continues execution regardless of failure, but logs the failure.
            `Run Keyword And Continue On Failure Some Keyword`
        `Run Keyword And Ignore Error` runs the keyword and ignores any failure without logging it.
            `Run Keyword And Ignore Error Some Keyword`

24. How do you implement BDD with Robot Framework?
        Robot Framework supports BDD (Behavior-Driven Development) by allowing test cases to be written in a behavior-driven style using keywords that reflect user stories or behaviors.
            *** Test Cases ***
            User Can Log In
            Given User is on login page
            When User enters valid credentials
            Then User is redirected to homepage

25.  What are some best practices for writing test cases in Robot Framework?
        - Use descriptive names for test cases and keywords.
        - Reuse keywords to avoid duplication.
        - Keep test cases and keywords simple and focused.
        - Use resource files for shared keywords and variables.
        - Organise test cases in a logical and maintainable directory structure.

26. How do you execute shell commands in Robot Framework?
        Use the `OperatingSystem` library to execute shell commands.
            `Run Process ls -l`

27. How would you test email functionality using Robot Framework?
        Use the `SMTP` and `IMAP` libraries to send and receive emails, then verify the content.    
            *** Settings ***
            Library SMTPLibrary
            Library IMAPLibrary
            *** Test Cases ***
            Test Email
            Open Connection smtp.example.com
            Send Message sender@example.com recipient@example.com Subject Body
            Open Mailbox imap.example.com user password
            List Messages ALL

28. How would you handle file uploads and downloads in Robot Framework?
        Use the `Choose File` keyword for uploads and verify downloads by checking the file system.
            `Choose File id=file_input path/to/file`

29.  How do you use the DateTime library in Robot Framework?
        The DateTime library provides keywords for handling date and time.
            `${date}= Get Current Date`

30. How do you use the String library in Robot Framework?
        The String library provides keywords for string manipulation.
            `${result}= Replace String Hello world world Robot Framework`

31. How do you use the Collections library in Robot Framework?
        The Collections library provides keywords for handling lists and dictionaries.
            `Append To List ${list} item`

32. How do you troubleshoot test failures in Robot Framework?
        Analyse logs and reports, debug scripts, verify locators, and check for environment issues.

33. What are some common issues faced in Robot Framework and their solutions?
        - Element not found: Use proper waits or check locators.
        - Timeout errors: Increase wait time or optimise scripts.
        - Environment issues: Ensure consistent test environments.

34. How do you debug Robot Framework test cases?
        - Use the `--debug` or `--loglevel TRACE` options to get detailed logs.
            `robot --loglevel TRACE tests/`

35. How do you handle flaky tests in Robot Framework?
        - Identify the root cause of flakiness, improve stability by adding waits or retries, and ensure a stable test environment.

36. How do you ensure test coverage in Robot Framework?
        - Use code coverage tools, define comprehensive test cases, and perform regular reviews to ensure all critical paths and scenarios are covered.

37. How do you schedule Robot Framework tests?
        - Use a CI/CD tool like Jenkins or cron jobs to schedule tests.
            `0 0 * * * cd /path/to/tests && robot -d reports`

38. How do you handle cross-browser testing in Robot Framework?
        - Use the SeleniumLibrary and pass different browser names to the `Open Browser` keyword.
            `Open Browser http://example.com chrome `
            `Open Browser http://example.com firefox`

39. 

### API Testing and HTTP Requests in Robot Framework
1.  How do you perform API testing with Robot Framework?
        Use the `RequestsLibrary` or `RESTInstance` library to perform HTTP requests and validate responses.

2.  How do you install RequestsLibrary for Robot Framework?
        Install RequestsLibrary using pip:
        `pip install robotframework-requests`

3.  How do you import RequestsLibrary in a test suite?
        Import the library in the `*** Settings ***` section:
            *** Settings ***
            Library RequestsLibrary

4.  How do you create a session in RequestsLibrary?
        Use the `Create Session` keyword:
            `${session} = Create Session my_session ${BASE_URL}`

5.  How do you send a GET request using RequestsLibrary?
        Use the `Get Request` keyword:
            `${response} Get Request my_session /api/resource`

6. How do you send a POST request using RequestsLibrary?
        Use the `Post Request` keyword:
            `${response} Post Request my_session /api/resource ${data}`

7.  How do you validate the status code of a response in RequestsLibrary?
        Use the `Should Be Equal As Numbers` keyword:
            `${status} Get Response Status ${response}`
            `Should Be Equal As Numbers ${status} 200 `

8.  How do you validate the JSON response body in RequestsLibrary?
        Use the `Get Response Json` keyword and appropriate assertions:
            `${json} Get Response Json ${response}`
            `Should Be Equal ${json['key']} expected_value`

9. How do you send a PUT request using RequestsLibrary?
        Use the `Put Request` keyword:
            `${response} Put Request my_session /api/resource ${data}`

10. How do you send a DELETE request using RequestsLibrary?
        Use the `Delete Request` keyword:
            `${response} Delete Request my_session /api/resource`

11. How do you send a PATCH request using RequestsLibrary?
        Use the `Patch Request` keyword:
            `${response} Patch Request my_session /api/resource ${data}`

12. How do you add headers to a request in RequestsLibrary?
        Use the `Create Session` keyword with the `headers` argument:
            `${headers} Create Dictionary Authorization=Bearer ${TOKEN}`
            `Create Session my_session ${BASE_URL} headers=${headers}`

13. How do you add query parameters to a request in RequestsLibrary?
        Include the query parameters in the URL or use the `params` argument:
            `${params} Create Dictionary key=value`
            `${response} Get Request my_session /api/resource params=${params}`
            `${response} Get Request my_session /api/resource?key=value`

14. How do you handle cookies in RequestsLibrary?
        Use the `Create Session` keyword with the `cookies` argument:
            `${cookies} Create Dictionary sessionid=12345`
            `${response} Create Session my_session ${BASE_URL} cookies=${cookies}`

15. How do you handle basic authentication in Requests?
        Use the `Create Session` keyword with the `auth` argument:
            `Create Session my_session ${BASE_URL} auth=${USERNAME}:${PASSWORD}`

16. How do you validate the response headers in RequestsLibrary?
        Use the `Get Response Headers` keyword and appropriate assertions:
            `${headers} Get Response Headers ${response}`
            `Should Be Equal ${headers['Content-Type']} application/json`

17. How do you handle redirects in RequestsLibrary?
        Use the `Create Session` keyword with the `allow_redirects` argument:
            `Create Session my_session ${BASE_URL} allow_redirects=${False}`

18. How do you send a multipart/form-data request using RequestsLibrary?**
        Use the `Post Request` keyword with the `files` argument:
           ` ${files} Create Dictionary file=@path/to/file`
            `${response} Post Request my_session /api/upload files=${files}`


19. How do you handle timeouts in RequestsLibrary?
        Use the `Create Session` keyword with the `timeout` argument:
            `Create Session my_session ${BASE_URL} timeout=${30}`

20. How do you handle SSL verification in RequestsLibrary?
        Use the `Create Session` keyword with the `verify` argument:
            `Create Session my_session ${BASE_URL} verify=${False}`

21. How do you validate the response time in RequestsLibrary?
        Use the `Get Response Elapsed Time` keyword and appropriate assertions:
            `${time} Get Response Elapsed Time ${response}`
            `Should Be Less Than ${time} ${500}`


### Selenium Library SeleniumLibrary and Web Testing
1.  What is SeleniumLibrary in Robot Framework?
        SeleniumLibrary is an external library for Robot Framework that provides keywords forweb testing, allowing interaction with web elements using the Selenium WebDriver.

2.  How do you install SeleniumLibrary?
        Install SeleniumLibrary using pip:
            `pip install robotframework-seleniumlibrary`

3.  How do you open a browser using SeleniumLibrary?
        Use the `Open Browser` keyword:
            `Open Browser ${URL} chrome`
            *** Settings ***
                Library SeleniumLibrary
                *** Test Cases ***
                Open Browser Test
                Open Browser http://example.com chrome

4.  How do you close a browser using SeleniumLibrary?
        Use the `Close Browser` keyword:
            `close Browser`

5.  How do you maximise a browser window using SeleniumLibrary?
        Use the `Maximise Browser Window` keyword:
            `Maximise Browser Window`

6.  How do you navigate to a URL using SeleniumLibrary?
        Use the `Go To` keyw
            `Go To ${URL}`

7.  How do you find an element by its ID using SeleniumLibrary?
        Use the `Find Element` keyword with the `id` locator strategy:
            `Find Element id=username_field`

8.  How do you input text into a text field using SeleniumLibrary?
        Use the `Input Text` keyword:
            `Input Text id=username_field ${USERNAME}`

9.  How do you click a button using SeleniumLibrary?
        Use the `Click Button` keyword:
            `Click Button id=login_button`

10. How do you select an option from a dropdown using SeleniumLibrary?
        Use the `Select From List By Label` keyword:
            `Select From List By Label id=dropdown Option 1`
            
11. How do you wait for an element to be visible using SeleniumLibrary?
        Use the `Wait Until Element Is Visible` keyword:
            `Wait Until Element Is Visible id=logout_button`

12. How do you wait for an element to be clickable using SeleniumLibrary?
        Use the `Wait Until Element Is Clickable` keyword:
            `Wait Until Element Is Clickable id=login_button`

13. How do you check if an element is visible using SeleniumLibrary?
        Use the `Element Should Be Visible` keyword:
            `Element Should Be Visible id=logout_button`

14. How do you check if an element is not visible using SeleniumLibrary?
        Use the `Element Should Not Be Visible` keyword:
            `Element Should Not Be Visible id=logout_button`

15. How do you get the text of an element using SeleniumLibrary?
        Use the `Get Text` keyword:
            `${text} Get Text id=welcome_message`

16. How do you verify the title of a page using SeleniumLibrary?
        Use the `Title Should Be` keyword:
            `Title Should Be Welcome Page`

17. How do you capture a screenshot using SeleniumLibrary?
        Use the `Capture Page Screenshot` keyword:
            `Capture Page Screenshot`
            
18. How do you handle alerts using SeleniumLibrary?
        Use the `Handle Alert` keyword:
            `Handle Alert ACCEPT`

19. How do you switch to a frame using SeleniumLibrary?
        Use the `Select Frame` keyword:
            `Select Frame id=frame_id`

20. How do you switch back to the main content from a frame using SeleniumLibrary?
        Use the `Unselect Frame` keyword:
            `Unselect Frame`

21. How do you handle dynamic elements in Robot Framework?
         Use dynamic locators, waits, and conditional statements to handle dynamic elements.

22. How do you handle timeouts in Robot Framework?
        Use the `Set Selenium Timeout` keyword to set timeouts for SeleniumLibrary.
            'Set Selenium Timeout 10 seconds'

23. How do you handle asynchronous operations in Robot Framework?
        Handle asynchronous operations by using keywords that wait for elements or conditions,
        such as `Wait Until Element Is Visible` or `Wait Until Keyword Succeeds`.


24. How do you locate elements using SeleniumLibrary?
        Use keywords like `Click Element`, `Input Text`, `Wait Until Element Is Visible`, etc., and specify locators using strategies like id, name, xpath, css selector, etc.
            `Click Element id=submit_button`

25. What are implicit and explicit waits in SeleniumLibrary?
        Implicit waits set a default wait time for finding elements, applicable to all element searches.
            `Set Selenium Implicit Wait 10 seconds`
        Explicit waits wait for specific conditions to be met before proceeding.
            `Wait Until Element Is Visible id=submit_button`
            
26. How do youwould you test a dynamic web table using Robot Framework?
        Use loops and conditional logic to interact with and verify table data.
        *** Test Cases ***
            Test Dynamic Table
            Open Browser ${URL} chrome
            ${rows}= Get Element Count //table[@id='table']/tbody/tr
            :FOR ${row} IN RANGE ${rows}
            \ ${cell}= Get Text //table[@id='table']/tbody/tr[${row}]/td[1]
            \ Should Be Equal ${cell} Expected Value


27. How would you automate a web form submission using Robot Framework?
        Write a test case that fills out the form fields and submits the form.
            *** Test Cases ***
            Test Form Submission
            Open Browser ${URL} chrome
            Input Text name John Doe
            Input Text email john.doe@example.com
            Click Button submit_button
            Element Should Be Visible success_message


28. How do you handle dynamic content in Robot Framework?
        Use keywords like `Wait Until Page Contains Element` or `Wait Until Element Is Visible` to handle dynamic content.
            `Wait Until Element Is Visible xpath=//button[@id='submit']`


29. How do you integrate Robot Framework with CI/CD tools?
        You can integrate Robot Framework with CI/CD tools like Jenkins, GitLab CI/CD, or GitHub Actions by creating pipeline scripts that install dependencies and execute Robot Framework tests.
                        `
                        pipeline {
                        agent any
                        stages {
                        stage('Install Dependencies') {
                        steps {
                        sh 'pip install -r requirements.txt'
                        }
                        }
                        stage('Run Tests') {
                        steps {
                        sh 'robot -d reports tests/'
                        }
                        }
                        }
                        post {
                        always {
                        archiveArtifacts artifacts: 'reports/*', allowEmptyArchive: true
                        junit 'reports/*.xml'
                        https://www.linkedin.com/in/anshulagarwal30/
                        }
                        }
                        }
                        `

# RealTime Scenario
1.  Python Library (Backend Logic)
# libraries/redfish_lib.py
```python
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class RedfishLib:

    def __init__(self):
        self.base_url = "https://192.168.1.100/redfish/v1"
        self.username = "root"
        self.password = "pass"
        self.headers = {"Content-Type": "application/json"} ##Request body is JSON format

    def get_power_state(self):
        url = f"{self.base_url}/Systems/system"
        response = requests.get(url, auth=(self.username, self.password), headers=self.headers, verify=False)
        response.raise_for_status()
        data = response.json()
        return data.get("PowerState")

    def reboot_system(self):
        url = f"{self.base_url}/Systems/system/Actions/ComputerSystem.Reset"
        payload = {"ResetType": "ForceRestart"}
        response = requests.post(url, json=payload, auth=(self.username, self.password), headers=self.headers, verify=False)
        return response.status_code
```
2.  Resource File (Custom Keywords = “Robot Functions”)
# resources/bmc_keywords.robot
*** Settings ***
Library    ../libraries/redfish_lib.py

*** Keywords ***
Get System Power State
    ${state}=    Get Power State
    [RETURN]    ${state}

Trigger System Reboot
    ${status}=    Reboot System
    Should Be Equal As Integers ${status}   200

3.  Common Utility Keywords
# resources/common_keywords.robot
*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Wait For System To Be ON
    [Arguments]    ${timeout}

    Wait Until Keyword Succeeds
    ...    ${timeout}
    ...    5 sec
    ...    Verify System Power ON


4.  Test Case File (Very Minimal)
# tests/power.robot

*** Settings ***
Resource    ../resources/bmc_keywords.robot
Resource    ../resources/common_keywords.robot

*** Test Cases ***
Verify Power State
    [Documentation]    Validate system power state is ON
    [Tags]    smoke    power
    ${state}=    Get System Power State
    Should Be Equal    ${state}    On

Reboot And Validate
    [Documentation]    Reboot system and verify it comes back ON
    [Tags]    regression    reboot
    Trigger System Reboot
    Wait For System To Be ON    60

''' power.robot
    ↓
bmc_keywords.robot
    ↓
common_keywords.robot
    ↓
redfish_lib.py
    ↓
Redfish API
'''