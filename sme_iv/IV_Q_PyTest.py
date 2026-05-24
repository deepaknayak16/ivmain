'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: find warning message in file python pytest
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import pytest

@pytest.fixture
def log_file_path():
    return "logfile.txt"  # Replace with the actual path to your file

def test_find_warning_messages(log_file_path):
    warning_messages = []
    try:
        with open(log_file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if "warning" in line.lower():
                    warning_messages.append((line_number, line.strip()))
    except FileNotFoundError:
        pytest.fail(f"Log file '{log_file_path}' not found.")
    
    # Assert warnings were found
    assert warning_messages, "No warning messages found in the file."

    # Print warnings for verification
    for line_number, message in warning_messages:
        print(f"Warning found at line {line_number}: {message}")

### API Testing with Pytest Parametrize
import pytest
import requests

BASE_URL = "https://api.example.com/login"

@pytest.mark.parametrize(
    "payload, expected_status",
    [
        ({"username": "admin", "password": "admin123"}, 200),
        ({"username": "user1", "password": "wrong"}, 401),
        ({"username": "", "password": "123"}, 400),
    ]
)
def test_login_api(payload, expected_status):
    response = requests.post(BASE_URL, json=payload)

    assert response.status_code == expected_status, f"Expected status {expected_status}, but got {response.status_code}"

##### Using Fixtures + Parametrization
import pytest
@pytest.fixture(params=[
    ("admin", "admin123"),
    ("user", "user123"),
    ("guest", "guest123")])

def user(request):
    return request.param

def test_login(user):
    username, password = user
    assert username is not None
    assert password is not None

#### Device Testing Scenario (IoT / BMC / Hardware)
import pytest
class DeviceClient:
    def get_power(self):
        return "ON"
    def reboot(self):
        return 200
    
@pytest.fixture
def device():
    return DeviceClient()

def test_device_power(device):
    assert device.get_power() == "ON"

def test_device_reboot(device):
    assert device.reboot() == 200



@pytest.fixture
def testserA():
    print("Setup A")
    yield
    print("Teardown A")

@pytest.fixture
def testserB(testserA):
    print("Setup B")
    yield
    print("Teardown B")

@pytest.fixture
def login(testserA):
    return "Login test"