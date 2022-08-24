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


list_filter = [] 
while(True):
    print("1.GET")
    print("2.POST")
    choose = int(input("choose : "))
    if choose == 1:
        p = input("params : ")
        print("1.Check filter")
        print("2.Easy payload brute force")
        print("3.Boolean sql")
        print("4.Error based sql")
        print("5.Your payload + filter bypass ")
        print("6.Time based sql")
        print("7.Numeric")
        choose_get = int(input("choose : "))
        if choose_get == 1 :
            Filter(url , header , p , list_filter)
        elif choose_get == 2:
            Get_Easy_Bf(url , header ,p)
        elif choose_get == 3:
            Get_Boolean(url , header , p)
        elif choose_get == 4:
            Get_Error_based(url , header ,p)
        elif choose_get == 5:
            Get_Filter(list_filter)
        elif choose_get == 6:
            Get_Time_based(url , header , p)
        elif choose_get == 7:
            Get_Numeric(url , header , p)
    elif choose == 2: # khoi tao data
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
            break
        elif choose_post == 2:
            Post_Easy_Bf(url , header , data, d , bf_data)






        

