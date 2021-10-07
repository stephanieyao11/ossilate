import requests
from pprint import pprint

username = "stephanieyao11"
url = f"https://api.github.com/users/{username}"
user_data = requests.get(url).json()
pprint(user_data)
print(user_data["followers"])
print(user_data["login"])


