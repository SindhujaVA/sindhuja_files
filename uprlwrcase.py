str1=input("Enter the string: ")
count1=0
count2=0
for i in str1:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:",count1)
print("The number of uppercase characters is:",count2)
