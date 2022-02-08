f=open("data.txt","w")
f.write("Hello everyone\nI am anjani prajapati.")
f.close()

f=open("data.txt","r")
print(f.read())
f.close()