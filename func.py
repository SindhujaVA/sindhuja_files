def smallcase(text):
 return text.lower()

def uppercase(text):
 return text.upper()

def greet(a):
 greetings=a("Hi good morning")
 print(greetings)

greet(smallcase)
greet(uppercase)