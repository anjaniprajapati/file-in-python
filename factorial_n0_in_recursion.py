def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

n1=int(input("enter any nu::"))
a=fact(n1)
print(n1,"OF FACTORIAL NUMBER",a)