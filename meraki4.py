f=open("meraki4.txt","r")
c=f.read()
my_file_1=open("delhi.txt","w")
my_file_2=open("shimla.txt","w")
my_file_3=open("another.txt","w")
k=c.split("\n")
i=0
while i<len(k):
    if "delhi" in k[i]:
        my_file_1.write(k[i])
        my_file_1.write("\n")
    elif "shimla" in k[i]:
        my_file_2.write(k[i])
        my_file_2.write("\n")
    else:
        my_file_3.write(k[i])
        my_file_3.write("\n")
    i+=1
f.close()
my_file_1.close()
my_file_2.close()
my_file_3.close()