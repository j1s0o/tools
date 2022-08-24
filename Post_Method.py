import requests
import string
import time
char = string.printable
session = requests.Session()


#Menu
def Post_Menu(url , header):
    print("1.Check filter")
    print("2.Easy payload brute force")
    print("3.Boolean sql")
    print("4.Your payload + filter bypass ")
    choose_post = int(input("choose : "))        
    c = int(input("How many data : "))
    d = []
    for i in range(0,c):
        d.append(input("Data %d : " %(i)))
    bf_data = int(input("Choose data to bf : "))
    data = {}
    for i in range(0,len(d)):
        if i != bf_data:
            add = {
                d[i] : input("%s : " %(d[i]))
            }
            data.update(add)
        else:
            add = {
                d[i] : "test"
            }
            data.update(add)
    if choose_post == 1:
        1 + 1
    elif choose_post == 2:
        Post_Easy_Bf(url , header , data, d , bf_data)
#Post Brute Force Data
def Post_Easy_Bf(url , header , data , d , bf_data):
    f = open("cheatsheet.txt" , "r")
    sp = input("Sepecial str :")
    for i in f:
        data[d[bf_data]] = i    
        post = session.post(url = url , headers= header , data=data)
        if sp not in post.text:
            print(len(post.text) , i )