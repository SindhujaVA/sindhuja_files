a=input("Enter a string:").strip()
countd=0
counta=0
for x in range(0,len(a)):
	if a[x].isdigit():
	 countd+=1
	elif a[x].isalpha():
	 counta+=1
print("No.of digits",countd)
print("No.of alphabets=",counta)