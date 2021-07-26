pwd=input("Enter the password: ")
p=len(pwd)
a=0
b=0
c=0
for i in pwd:
    i.islower()
    a=1
    i.isupper()
    b=1
    i.isdigit()
    c=1      

if p>6 and p<=16 and a==1 and b==1 and c==1:
  print("Password is validated")
else:
  print("Password should contain:\nAtleast 1 letter between [a-z] and 1 letter between [A-Z] \nAtleast 1 number between [0-9]\nAtleast 1 character[$#@]\nMinimum length 6 characters.\nMaximum length 16 characters")



