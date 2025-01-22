import requests

people = requests.get("http://api.open-notify.org/astros.json")
json = people.json()

print(json)

print(f"The people currently in space are:")
for p in json["people"]:
    print(p["name"])
