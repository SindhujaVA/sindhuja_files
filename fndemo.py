#Function
def function_name(arguments):
	return True
print (function_name('a'))


def display():
	print("Hi!")
display()


def my_info():
	return{"name":"Sindhuja", "age":25, "deg":"MCA"}
print(my_info())



def fn1(num):
 if num>10:
  return f"{num} is greater than 10"
 else:
  return f"{num} is not greater than 10"

a=int(input("Enter a number: "))
b=fn1(a)
print(b)

def myfn():
	pass


def func2(*a):
    c = 0
    for i in a:
        c+=i
    return c

a = func2(1,2,3,4)
print(f"{a} is the sum of given numbers")

def func3(**a):
    for key,value in a.items():
        print(key,value)

func3(name="tom",age = 22)



