import requests

url = "http://localhost:8000/mcp/"

headers = {
    "Accept": "application/json , text/event-stream",
    
}

# Calling the get_weather tool

body = {
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
        "name": "get_weather",
        "arguments": {
            "city": "New York"
        }
    },
    "id": 1
}

response = requests.post(url, headers=headers, json=body)
for line in response.iter_lines():
    if line:
        print(line)