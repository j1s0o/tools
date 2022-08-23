import requests
import string
import time
char = string.printable
session = requests.Session()



#Post Brute Force Data
def Post_Easy_Bf(url , header , data , d , bf_data):
    f = open("cheatsheet.txt" , "r")
    sp = input("Sepecial str :")
    for i in f:
        data[d[bf_data]] = i    
        post = session.post(url = url , headers= header , data=data)
        if sp not in post.text:
            print(len(post.text) , i )