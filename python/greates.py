a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))

if (a>b)and(a>c):
    print(a," greater than ",b,c)
elif (b>a)and(b>c):
    print(b ,"greater than ",a,c)
else :
    print(c," greater than ",a,b)
