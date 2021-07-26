#Printing average for Marklist of five subjects

marks=input("Enter the marks for five subjects").split()
marklist=[]
for i in marks:
	marklist.append(int(i))

print(sum(marklist)/len(marklist))

