def small_case(text):
    return text.lower()

def upper_case(text):
    return text.upper()

def greet(func):
    greetings = func("hi good morning")
    print(greetings)

greet(small_case)
greet(upper_case)

def a():
    print("i m function a")

def b():
    print("i m function b")
    return a
    
c= b()
c()