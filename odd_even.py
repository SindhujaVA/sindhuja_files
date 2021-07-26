n1=int(input("Enter the number1: "))
n2=int(input("Enter the number2: "))
evenlist=[]
oddlist=[]
if ((n1%2)==0) :
   evenlist.append(n1)
else: oddlist.append(n1)

if ((n2%2)==1):
    oddlist.append(n2)
else: evenlist.append(n2)

print("Odd list is{}".format(oddlist))
print("Even list is{}".format(evenlist))   

