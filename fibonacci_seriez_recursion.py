def fibo(a):
    if a==1:
        return 0
    if a==2:
        return 1
    return (fibo(a-1)+ fibo(a-2))

n=int (input("enter any number::"))
for i in range(1,n+1):
    print(fibo(i))






def fibo():
    n=int(input("enter any number::"))
    i=0
    a=0
    b=1
    while i<=n:
        a=b
        b=i
        i=a+b
        print(i)
fibo()