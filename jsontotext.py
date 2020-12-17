import json
import requests
responce=requests.get("https://api.github.com/repos/laravel/laravel/stargazers?per_page=100&page=2")
data=responce.json()

f = open("demofile2.txt", "a")
for i in data:
    print(i["login"])
    f.write(i["login"]+"\n")
f.close()

