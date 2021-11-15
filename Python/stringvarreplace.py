str=input("Enter the string ")
str=list(str)
ch=str[0]
str[0]=str[-1]
str[-1]=ch
str1=' '.join(str)
print(str1)
