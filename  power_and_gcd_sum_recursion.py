          #POWER USE OF RECURSION


def power(n,n1):
    if n1==0:
        return 1
    else:
        return n*power(n,n1-1)

x=int(input("enter any number::"))
y=int(input("enter any power::"))
a=power(x,y)
print(x,"**",y,"=",a)



# def gcd(n,n1):
#     if n1==0:
#         return 1
#     else:
#         return(gcd(n1,n%n1))

# a=int(input("enter any larg no::"))
# b=int(input("enter any small no::"))
# s=gcd(a,b)
# print(b,a,s)



# def sum(list):
#     if len(list)==1:
#         return list[0]
#     else:
#         return list[0]+(sum(list[1:]))
# a=[1,2,3,4,5,6]
# s=sum(a)
# print(s)