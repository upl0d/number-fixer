import requests

response = requests.get("https://api.github.com")
print(response.status_code)
if not response.status_code == 200:
    print(f"Error {response.status_code}")
else:
    print(f"Connection [OK] Status code [{response.status_code}]")
