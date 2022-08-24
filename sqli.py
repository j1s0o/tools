import requests
import string
import time
from Get_Method import *
from Post_Method import *

char = string.printable
session = requests.Session()

url = input("url hia :  ")
print("url : "  , url)
cookie = input("cookie neu co : ")
header = {
    'Cookie' : cookie
}
print(cookie)

while(True):
    print("1.GET")
    print("2.POST")
    choose = int(input("choose : "))
    if choose == 1:
        p = input("params : ")
        Get_Menu(url , header , p)
    elif choose == 2: # khoi tao data
        Post_Menu(url , header)        






        

