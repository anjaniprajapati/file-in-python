f=open("people3.txt","r")
data=f.read()
f.close()
print(data)
i=0
c=0
while i< len(data):
    if data[i]=="\n":
        c+=1
    i+=1
print(c)
