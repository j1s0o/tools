c = int(input("How many data : "))
d = []
for i in range(0,c):
    d.append(input("Data %d : " %(i))) 

data = {

}
for i in range(0,len(d)):
    if i != 0:
        add = {
            d[i] : input("%s : " %(d[i]))
        }
        data.update(add)
print(data)