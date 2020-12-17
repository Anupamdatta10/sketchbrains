import json
import requests
import unidecode
responce=requests.get("https://api.github.com/repos/laravel/laravel/stargazers?per_page=100&page=2")
data=responce.json()

f = open("demofile2.txt", "a")
for i in data:
    url="https://api.github.com/users/"+i["login"]
    name=requests.get(url)
    fullname=name.json()
    print(fullname["name"])
    f.write(str(i["login"])+", name="+str(fullname["name"])+"\n")
f.close()

