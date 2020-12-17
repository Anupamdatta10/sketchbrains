import json
import requests
import unidecode
responce=requests.get("https://api.github.com/repos/laravel/laravel/stargazers?per_page=100&page=2")
data=responce.json()

f = open("demofile2.txt", "a",encoding="utf-8")

for i in data:
    print(str(i["login"]))
    url="https://api.github.com/users/"+i["login"]
    name=requests.get(url)
    fullname=name.json()
    n=str(fullname["name"])
    firstname=n.split()
    if len(firstname)==1:
        f.write(str(i["login"])+", firstname="+firstname[0]+", lastname=none"+"\n")
    else:
        f.write(str(i["login"])+", firstname="+firstname[0]+", lastname="+firstname[-1]+"\n")
    

f.close()

