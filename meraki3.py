
my_file=open("meraki3.txt","w")
list = ["Kotak\n", "HDFC\n", "RBL\n", "SBI\n", "Bank of Baroda\n"]
my_file.writelines(list)
my_file.close()

f=open("meraki3.txt","r")
print(f.read())
f.close()