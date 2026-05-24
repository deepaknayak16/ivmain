
'''
Common HTTP Response Codes (You MUST know these)
1xx — Informational
        100	Continue
        101	Switching Protocols
        102	Processing
        103	Early Hints
✅ Success
        200 OK → Request successful (GET, POST)
        201 Created → Resource created successfully
        204 No Content → Success but no data returned
3xx — Redirection
        300	Multiple Choices
        301	Moved Permanently
        302	Found
        303	See Other
⚠️ Client Errors (Your mistake)
        400 Bad Request → Invalid input
        401 Unauthorized → Authentication required
        403 Forbidden → No permission
        404 Not Found → Resource doesn’t exist
        409 Conflict → Resource exist
❌ Server Errors
        500 Internal Server Error → Server crashed / unknown issue
        502 Bad Gateway → Upstream failure
        503 Service Unavailable → Server overloaded/down

Status      Code	        Meaning	Sync/Async
2xx	        Success	        Mostly synchronous
202	        Accepted	    Asynchronous
4xx	        Client error	Synchronous
5xx	        Server error	Synchronous

    synchronous because response is returned immediately
    asynchronous processing where server accepts request and processes it later in background.

Common HTTP Methods (You MUST know these)
GET → Retrieve data from the server
POST → Create a new resource on the server
PUT → Update an existing resource on the server (Replace the whole document.)
DELETE → Remove a resource from the server
PATCH → Partially update a resource on the server (Edit only one line.)
HEAD → Retrieve headers without the body (like GET but no content)
OPTIONS → Describe communication options for the target resource
CONNECT → Establish a tunnel to the server
TRACE → Perform a message loop-back test along the path to the target resource   
'''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: dump vs dumps in Python (from the json module)
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#| Function  | Input                | Output           | Usage                      |
#| --------- | -------------------- | ---------------- | -------------------------- |
#| `dump()`  | Python object + file | Writes JSON file | Save JSON directly to file |
#| `dumps()` | Python object        | JSON string      | Store/print/send JSON data |

## json.dump() -> Writes JSON data directly to a file object.
import json
import types
data = {"name": "Deepak", "age": 28}
with open("data.json", "w") as f:
    json.dump(data, f)   # writes JSON into file O/P {"name": "Deepak", "age": 28}

## json.dumps() ->Converts Python object → JSON string.
import json
data = {"name": "Deepak", "age": 28}
json_str = json.dumps(data)  
print(json_str) 

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: json.load() vs json.loads()
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#| Method         | Used For                    | Input                             | Output                           |
#| -------------- | --------------------------- | --------------------------------- | -------------------------------- |
#| `json.load()`  | Read from a **file object** | File object (`open('file.json')`) | Python object (dict, list, etc.) |
#| `json.loads()` | Read from a **string**      | JSON **string**                   | Python object                    |
#Example — load()
import json
# contents of data.json
# {"name": "Deepak", "age": 25, "skills": ["Python", "IoT"]}
with open('data.json', 'r') as f:
    data = json.load(f)   # load → file object
    print(data)
#Example — loads()
import json
json_str = '{"name": "Deepak", "age": 25, "skills": ["Python", "IoT"]}'
data = json.loads(json_str)   # loads → string
print(data)

#| Action         | File          | String         |
#| -------------- | ------------- | -------------- |
#| **Read JSON**  | `json.load()` | `json.loads()` |
#| **Write JSON** | `json.dump()` | `json.dumps()` |
#🔹 The trailing “s” stands for “string”.
#🔹 So:
#loads() → Load from string
#dumps() → Dump to string

import ast

js = '''{'deepak': 'eng', 'Nayak':'8'}'''

# Convert string to dictionary safely
data = ast.literal_eval(js)

# Access values
print("Value of deepak:", data['deepak'])
print("Value of Nayak:", data['Nayak'])


logs = [
    ("2009-10-31 01:48:52", "A1", 23.56),
    ("2009-10-31 02:48:52", "A1", 30.00),
    ("2009-10-31 03:48:52", "A2", 28.75),
    ("2009-10-31 04:48:52", "A3", 19.80)
]

for log in logs:
    timestamp, sensor_id, value = log
    if value > 25:
        print(timestamp, sensor_id, value)  #2009-10-31 03:48:52 A2 28.75
        print(log) # ('2009-10-31 03:48:52', 'A2', 28.75)
data_s1 = {
    "sensors": [
        {"types": "temperature", "value": 25.6},
        {"types": "humidity", "value": 60},
        {"types": "temperature", "value": 28.2},
        {"types": "pressure", "value": 1012}
    ]
}
# Extract all temperature values
temp_value = [sensor["value"] for sensor in data_s1["sensors"] if sensor["types"] == "temperature"]
print(temp_value) #[25.6, 28.2]
temp_types =[sensor["types"] for sensor in data_s1["sensors"] if sensor["value"] <= 30]
print(temp_types) #output: ['temperature', 'temperature']

response = {
    "users": [
        {"id": 1, "Active": True},
        {"id": 2, "Active": False},
        {"id": 3, "Active": True}
    ]
}
active_ids = [user["id"] for user in response["users"] if user["Active"]] # we can active == true
print(active_ids) #[1, 3]
print(response["users"][0]["Active"]) #True

#How do you handle JSON decoding errors?
try:
    data = json.loads('{"name": "Deepak", }')
except json.JSONDecodeError as e:
    print("Invalid JSON:", e)

########## API CALLING EXAMPLE ########################
import requests
import urllib3
import logging

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class RedfishLib:
    def __init__(self):
        self.base = "https://192.168.1.100/redfish/v1"
        self.session = requests.Session()
        self.session.auth = ("root", "pass")
        self.session.headers.update({"Content-Type": "application/json", "Accept": "application/json"})

    def get_power_state(self):
        try:
            url = self.base + "/Systems/system/"
            response = self.session.get(url, verify=False, timeout=10)
            response.raise_for_status()
            power_state = response.json().get("PowerState")
            logging.info(f"Power State: {power_state}")
            return power_state
        except Exception as e:
            logging.error(f"Failed to get power state: {e}")
            return None

    def reboot_system(self):
        try:
            url = self.base + "/Systems/system/Actions/ComputerSystem.Reset"
            payload = {"ResetType": "ForceRestart"}
            response = self.session.post(url, json=payload, verify=False, timeout=15)
            response.raise_for_status()
            logging.info(f"Reboot successful: {response.status_code}")
            return response.status_code
        except Exception as e:
            logging.error(f"Reboot failed: {e}")
            return 500

    def set_power_state(self, url):
        try:
            payload = {"status": "on"}
            response = self.session.patch(url, json=payload, verify=False, timeout=10)
            response.raise_for_status()
            logging.info(f"PATCH successful: {response.status_code}")
            return response.status_code
        except Exception as e:
            logging.error(f"PATCH failed: {e}")
            return 500

    def delete_resource(self, url):
        try:
            response = self.session.delete(url,verify=False,timeout=10)
            response.raise_for_status()
            logging.info(f"DELETE successful: {response.status_code}")
            return response.status_code
        except Exception as e:
            logging.error(f"DELETE failed: {e}")
            return 500

'''
requests.Session() > Connection pooling > Persistent authentication > Better performance > Reduced overhead > Cookie/session reuse
Yes, using requests.Session() and calling self.session.get() is the correct and scalable approach. Authentication and headers are handled at session level, 
so they don't need to be repeated in each request. Adding timeout ensures stability, and verify=False is acceptable in environments. 
include raise_for_status() for proper error handling
Exception handling is important to avoid abrupt failures and provide proper logging, debugging, and recovery handling during API failures.
'''