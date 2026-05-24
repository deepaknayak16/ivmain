'''
BMC Test Automation Framework (Hybrid)
├── CI/CD Pipeline (Jenkins / GitLab CI)
├── Test Execution Layer
│   ├── Robot Framework (High-level suites)
│   └── Pytest (Low-level + libraries)
├── Core Libraries Layer (Python)
│   ├── BMC Communication (Redfish, IPMI, SSH, Serial)
│   ├── Hardware Abstraction Layer (HAL)
│   ├── Error Injection & RAS Tools
│   └── Common Utilities (Logging, FFDC, Reporting)
├── Test Data Layer
├── Resources & Keywords
└── Test Reports & Dashboards


bmc-hardware-test-framework/
├── config/
│   ├── environments/          # dev, qa, lab1, production
│   ├── credentials.yaml
│   └── testbed.yaml
├── libraries/                 # Python libraries (used by both)
│   ├── bmc_lib/
│   │   ├── redfish_client.py
│   │   ├── ipmi_client.py
│   │   ├── serial_console.py
│   │   └── sensor_manager.py
│   ├── hardware/
│   │   ├── power_control.py
│   │   ├── error_injection.py
│   │   └── ras_utils.py
│   └── utils/
├── resources/                 # Robot resources & keywords
│   ├── common_keywords.robot
│   ├── redfish_keywords.robot
│   ├── ipmi_keywords.robot
│   └── hardware_keywords.robot
├── tests/
│   ├── pytest/                # Low-level & API tests
│   │   ├── conftest.py
│   │   ├── test_redfish/
│   │   ├── test_sensors/
│   │   └── test_firmware_update/
│   └── robot/                 # High-level functional tests
│       ├── smoke/
│       ├── regression/
│       ├── ras/
│       └── stability/
├── results/                   # Auto-generated reports
├── logs/
├── pytest.ini
├── robot.yaml                 # or test suite files
└── requirements.txt




'''
import requests

# Define API details
url = "https://redfish-server-ip/redfish/v1/Managers/1/VirtualMedia/CD"
headers = {"Content-Type": "application/json"}
auth = ("username", "password")  # Replace with your credentials

# Payload for mounting ISO
payload = {
    "Image": "http://example.com/iso/my_update.iso",
    "Inserted": True,
    "WriteProtected": True
}

# Send the POST request
response = requests.post(url, json=payload, headers=headers, auth=auth, verify=False)

if response.status_code == 200:
    print("ISO mounted successfully!")
else:
    print(f"Failed to mount ISO: {response.status_code}, {response.text}")

task_url = "https://redfish-server-ip/redfish/v1/TaskService/Tasks/1"
response = requests.get(task_url, headers=headers, auth=auth, verify=False)

if response.status_code == 200:
    task_status = response.json()
    print(f"Update Status: {task_status['TaskState']}")
else:
    print(f"Failed to retrieve task status: {response.status_code}, {response.text}")

#--------------------------------------------------------------------
import serial
import time

ser = serial.Serial('COM3', 9600, timeout=1)

time.sleep(2)

ser.write(b'Ping\n')

while True:
    if ser.in_waiting:
        response = ser.readline().decode().strip()
        print("Response:", response)
        break

ser.close()
