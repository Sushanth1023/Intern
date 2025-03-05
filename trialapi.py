import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

response = requests.get("https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow", verify=False)
print("Status Code:", response.status_code)
print("Response Text:", response.text)

try:
    data = response.json()
    print(data)
except json.JSONDecodeError:
    print("Failed to decode JSON response")