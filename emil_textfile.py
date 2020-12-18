import json
import requests
import unidecode
k=0

f = open("data1.txt", "a",encoding="utf-8")
responce=requests.get("https://api.github.com/repos/laravel/laravel/stargazers?per_page=100&page=2")
k+=1
data1=responce.json()
for i in data1:
    
    nameurl="https://api.github.com/users/"+i["login"]#get the login name
    k+=1
    nresponce=requests.get(nameurl)
    data=nresponce.json()
    name=str(data["name"])
    eurl="https://api.github.com/users/"+i["login"]+"/events/public"#get the email json
    k+=1
    eresponce=requests.get(eurl)
    edata=eresponce.json()
    email=json.dumps(edata)
    if 'email'in email:#check if emil exist or not
        
        e=email.find('email')#extract email
        com=email[e:(e+100)]
        l=com[7:com.find(',')]
        #email=str(edata[10]["payload"]["commits"][0]["author"]["email"])
        f.write(name+"|email:"+l+"\n")
    if k>25:
        break
    
print("done")
f.close()
#for each entry 3 api call are going on so after some time get blocked
#so i hv used a break after 25 api calls