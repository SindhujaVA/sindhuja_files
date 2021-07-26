"""Data type
declaration and printing
"""
a=10
print(a)
print(type(a))
print(float(a))               #typecasting
b="laptop"
print(type(b))      

num=(1,2,3,4,5)
print(num[0:2])               #slicing
print(num[-1])
print(num[2:])
print(num)

name="My Name is Sindhuja"     
name1=name.split()            #split
name2=name.split("is")
print(name1,name2)
name3=''.join(name)    
print(name3)                   #join


y=0                            #boolean
print(bool(y))
k=2
print(bool(k))


str1="hi"                       #string concatenation
str2="how r u"
str3=str1+str2
print(str3)

print("This is a book named \"Programming in java\" ")
print("hi\nall")                #escape characters
print("\thello")

s="chair"                       #string functions
print(s.upper(), s.lower(), s.replace('c','C'), s.capitalize(), s.isnumeric(),s.isalpha())


name=input("Enter your name: ")
age=int(input("Enter your age: "))        #input function           
print(f"Your name is {name} and age is {age}")


		