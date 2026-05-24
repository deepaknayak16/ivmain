# Process Library, Pytest Fixtures, Parameterization, Markers & Commands
framework/
│
├── tests/
│   ├── api/
│   ├── ui/
│   ├── device/
│
├── pages/ (UI)
├── clients/ (API clients)
├── libraries/ (Python backend logic)
├── resources/ (Robot / keywords if hybrid)
│
├── utils/
│   ├── logger.py
│   ├── config.py
│   ├── helpers.py
│
├── testdata/
│   ├── login.json
│   ├── users.yaml
│
├── conftest.py
├── pytest.ini
└── requirements.txt
## What is the Process Library and Why Do We Need It?
   ### What is a Process Library?
   A **Process Library** is a structured collection of predefined processes, best practices, procedures, and workflows used to standardize and guide operations within an organization. It is commonly used in software development, business management, and engineering systems to ensure **consistency** and **efficiency**.

   In software development and operating systems, a Process Library also refers to modules or libraries that provide functionalities for managing processes — such as creating, monitoring, synchronizing, and terminating them.

   ### Why Do We Need a Process Library?

   1. **Standardization**  
      Ensures all teams follow a consistent approach, improving predictability and reducing errors.
   2. **Efficiency**  
      Reuses proven processes instead of reinventing the wheel, saving time and resources.
   3. **Collaboration**  
      Acts as a shared reference point, improving communication across team members.
   4. **Error Reduction**  
      Uses tested and validated processes, minimizing mistakes.
   5. **Scalability**  
      Makes it easier to replicate and scale operations as the organization grows.
   6. **Knowledge Management**  
      Preserves institutional knowledge even when team members change.

   ### Examples of Process Libraries

   - **Business Process Libraries**: Procurement, HR, Customer Service workflows.
   - **Software Development**: Agile, Scrum, Waterfall templates.
   - **Engineering**: Hardware debugging, validation, and manufacturing processes.
   - **Operating Systems**: `libc` (C), Python’s `subprocess` / `multiprocessing`, Node.js `child_process`.

   ### Use in Programming
   Process libraries typically provide utilities for:
   - Process Creation (e.g., `subprocess.run()`)
   - Inter-Process Communication (IPC)
   - Process Monitoring
   - Process Termination

## Pytest Concepts
   ### Q. What is a fixture?
   A **fixture** is a setup function that Create the required environment or resources for something before the test, and destroy/clean it after the test.
      Key Features:
      Automatic invocation
      Different scopes: function (default), class, module, session
      Supports setup + teardown using yield
      Can be parameterized
   #### How can a fixture be automatically run?
      A fixture can run automatically by using: autouse=True inside the fixture decorator.
      @pytest.fixture(autouse=True)
   #### Simple Fixture** 
      ```python
      import pytest

      @pytest.fixture
      def setup_data():
         return {"name": "Alice", "age": 30}

      def test_user(setup_data):
         assert setup_data["name"] == "Alice"
      ```
   #### Parameterized Fixture**
      ```python
      @pytest.fixture(params=["Alice", "Bob", "Charlie"])
      def user_name(request):
         return request.param
      ```
   #### Multiple Fixture with Scope
      ```python
      @pytest.fixture(scope="module")
      def db_connection():
         print("Opening DB connection")
         yield "DB Connection"
         print("Closing DB connection")

         @pytest.fixture(scope="session")
         def setup():
            print("Setup")
      ``` 
      ```python  
         # Run all tests
         pytest
         # Run specific file
         pytest test_file.py
         # Run specific test function
         pytest test_file.py::test_function_name
         # Verbose mode
         pytest -v
         # Stop after first failure ::: Stops execution immediately when a test fails
         pytest -x
         Run with specific marker   @pytest.mark.smoke  #@pytest.mark.run1  
         pytest -m smoke
         pytest -m run1
         # Quiet mode
         pytest -q
         # Run with coverage (requires pytest-cov)
         pytest --cov=. --cov-report=html
         # Run specific testfunction from 10 testcase only number 3 testfinction want tu run from test class
         # Professional way
         pytest test_file.py::Test_class::test_03_reboot
         # Run by keyword (-k)
         pytest -k "test_03_reboot" 
         # Run full class but filter one test
         pytest test_file.py -k "reboot"
         # Run Multiple testcase
         pytest test_file.py::test_case1 test_file.py::test_case2 test_file.py::test_case3   
      ```
      
## Q. Can we create and tear down instances within one fixture?
**Yes.** In **pytest**, you can handle both setup and teardown in a single fixture using the `yield` statement.

      ```python
      import pytest
      @pytest.fixture
      def resource_fixture():
         # Setup phase
         print("\n[Setup] Creating instance...")
         instance = {"name": "TestInstance", "status": "Running"}

         yield instance  # Resource is passed to the test

         # Teardown phase
         print("\n[Teardown] Destroying instance...")
         instance["status"] = "Destroyed"
         print(f"Instance status: {instance['status']}")

      def test_resource_usage(resource_fixture):
         print(f"Using resource: {resource_fixture}")
         assert resource_fixture["status"] == "Running"
      ```
## What is scope Pytest?
      reduce repeated setup , improve test speed, manage resources efficiently
      ---------------------------------------------------------------------
      | Scope      | Created                      | Destroyed              |
      | ---------- | ---------------------------- | ---------------------- |
      | `function` | Before each test function    | After each test        |
      | `class`    | Once per test class          | After class ends       |
      | `module`   | Once per module/file         | After file ends        |
      | `package`  | Once per package             | After package ends     |
      | `session`  | Once for entire test session | After all tests finish |

## Q. What are the Markers Available in Pytest?
Markers are used to add metadata to test functions for categorization, skipping, failing, etc.
*** Bulit-in Markers ***
   ***Marker,                          Purpose,                                     Example
   @pytest.mark.skip,            Skip test unconditionally,             "@pytest.mark.skip(reason=""Not ready"")"
   @pytest.mark.skipif,          Skip based on condition,               "@pytest.mark.skipif(sys.version_info < (3,9))"
   @pytest.mark.xfail,           Expected to fail,                      "@pytest.mark.xfail(reason=""Known bug"")"
   @pytest.mark.parametrize,     Run with multiple parameters,          "@pytest.mark.parametrize("a, b, expected", [(1, 2, 3),(3, 4, 7)])
   @pytest.mark.timeout,         Set maximum execution time,            "@pytest.mark.timeout(2)
   ### Q:: How do you skip a test in Pytest?
      ```python
      @pytest.mark.skipif(sys.platform == "win32",
                    reason="Does not run on Windows")
      def test_linux_only():
         pass
      ```
   ### Custom Markers Q:: How do you create a customized marker?
      ```python
      @pytest.mark.smoke
      def test_login():
         assert 1 + 1 == 2

      @pytest.mark.regression
      def test_checkout():
         assert 2 * 2 == 4
      ```
      pytest -m smoke
      pytest -m "smoke or regression"

   ### pytest.ini
   [pytest]
   markers =
      smoke: smoke tests
      regression: regression tests
   ### Assign multiple marker 
      Method 1 — Multiple decorators (most common)

      ```python
         @pytest.mark.smoke
         @pytest.mark.regression
         @pytest.mark.login
         def test_user_login():
            assert True
      ```
      pytest -m "smoke and login"

      ```python
         pytestmark = [pytest.mark.smoke, pytest.mark.api]
         def test_one():
            pass
         def test_two():
            pass
      ```

      ```python
         @pytest.mark.parametrize(
            "value",
            [
               pytest.param(1, marks=[pytest.mark.smoke, pytest.mark.fast]),
               pytest.param(2, marks=pytest.mark.regression),
            ]
         )
         def test_values(value):
            assert value > 0
      ```

## Q. Parameterization
   Parameterization allows running the same test with multiple datasets.
   *** Benefits of Parameterization ***
      1. Improved Test Coverage  >  Covers multiple scenarios and edge cases.
      2. Code Reusability        >  Avoids writing duplicate test cases.
      3. Reduced Redundancy      >  Keeps test code clean.
      4. Flexibility             >  Easy to add new test data.
      5. Efficiency              >  Saves time and effort.
   ```python
   import pytest
   @pytest.mark.parametrize("a, b, expected",[(1, 2, 3),(3, 4, 7),(5, 6, 11)])
   def test_addition(a, b, expected):
      assert a + b == expected
   ```
## Mocking & Isolation


## Hooks (Very Important for Seniors)
   ## What are Pytest hooks?
   Hooks are special functions that allow you to customize the behavior of pytest at various stages of the testing process. They are defined in a `conftest.py` file and can be used to modify test collection, setup, teardown, and reporting.

## Parallel Execution
   ## How do you run tests in parallel?
   Use the `pytest-xdist` plugin.
   1. Install the plugin:
      `pip install pytest-xdist`
   2. Run tests across multiple CPUs:
      `pytest -n 4`  # Runs tests using 4 workers
   3. Run tests using all available CPUs:
      `pytest -n auto`

## Conftest.py
   ### What is conftest.py?
   `conftest.py` is a configuration file for pytest that allows you to share fixtures, hooks, and plugins across multiple test files in a directory without needing to import them.
   - Fixtures defined in `conftest.py` are automatically discovered by pytest.
   - It is used to define project-wide setup/teardown logic.

## Pytest-html Reporting
   ### How do you generate HTML reports?
   1. Install the plugin:
      `pip install pytest-html`
   2. Run tests with the report flag:
      `pytest --html=report.html`
      
## Flaky test handling
   ### What are flaky tests? 
   Flaky A flaky test is a test that: sometimes passes ❌ sometimes fails ❌ without any code change.
   ### How do you handle flaky tests?
   Retry mechanism (pytest-rerunfailures), Increase wait stability, Mock unstable dependencies, Remove timing dependency
   1. Install the plugin:
      `pip install pytest-rerunfailures`  
   2. Add xplicit waits instead of sleep `WebDriverWait(driver, 10).until(...)`

## Debug  
   ## What is --tb=short?
      Short traceback format.
   ### What is --lf?
      Run last failed tests.
   ### What is --ff?
      Run failed tests first.
   ### Debugging Configuration (pytest.ini)
      [pytest]
      addopts = --tb=short --lf
   ### Enter debugger on failure
      `pytest test_file.py::test_name --pdb`
   ### Show full logs
      `pytest --show-capture=all`
   ### What is pytest.set_trace()?
      Debugging breakpoint.
   ### What is pytest.fail()?
      Forcefully fail test.