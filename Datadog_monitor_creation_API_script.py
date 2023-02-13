import requests
import json

# Your Datadog API key
api_key = "YOUR_API_KEY"

# The URL for creating monitors in Datadog
url = "https://api.datadoghq.com/api/v1/monitor"

# Prompting the user for monitor type
monitor_type = input("Enter monitor type (metric alert/service check alert/event alert): ")

# Prompting the user for the monitor name
monitor_name = input("Enter monitor name: ")

# Prompting the user for the monitor message
monitor_message = input("Enter monitor message: ")

# Prompting the user for the monitor query
monitor_query = input("Enter monitor query: ")

# Prompting the user for the no_data_timeframe
no_data_timeframe = int(input("Enter the no_data_timeframe (in minutes): "))

# Prompting the user for notify_no_data
notify_no_data = input("Enter 'True' if you want to receive notifications for no data, 'False' otherwise: ")

# The payload for the API request
payload = {
  "type": monitor_type,
  "query": monitor_query,
  "name": monitor_name,
  "message": monitor_message,
  "notify_no_data": eval(notify_no_data),
  "no_data_timeframe": no_data_timeframe
}

# Setting up the API request headers
headers = {
    'Content-Type': 'application/json',
    'DD-API-KEY': api_key
}

# Sending the API request to create the monitor
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Checking if the request was successful
if response.status_code == 201:
    print("Monitor created successfully")
else:
    print("Failed to create monitor")
    print("Response:", response.json())
