import datetime
class Library():
	
    def __init__(self,booklist):
        self.booksavailable=booklist

    def disp(self):
        print("Welcome to Chennai Public Library !!!")
        for book in self.booksavailable:
           print(book)
    
    def lendbook(self,requestedbook):
        
        if requestedbook in self.booksavailable:
            print("You can take the requested book from the library")
        else:
            print("Sorry the requested book is currently not available, please enter any other book name")

    def addbook1(self,returnedbook):
        self.booksavailable.append(returnedbook)
        print("Thanks for returning the borrowed book!")
    
    def addbook2(self,donatedbook):
        self.booksavailable.append(donatedbook)
        print("Thanks for donating a book!")

           
class User():

    def adduser(self):
        name=input("Enter your name: ")
        mobileno=input("Enter your mobile number: ")
        email=input("Enter your email id: ")
        print(f'User Name:{name},Mobile No:{mobileno},Email id:{email}')
       
    def BorrowBook(self):
        print("Enter the name of the book to borrow: ")
        self.book=input()
        s=[]
        s.append(self.book)
        d=datetime.datetime.today()
        tdelta=datetime.timedelta(days=15)
        print(f'Books borrowed by the user :{s} on {d} and should be returned after 15 days,that is on{d+tdelta}')
        return self.book
     
    def ReturnBook(self):
        print("Enter the name of the book to return: ")
        self.book=input()
        r=[]
        r.append(self.book)
        print(f'Books returned by the user :{r}')
        return self.book
        
    def DonateBook(self):
        print("Enter the name of the book to donate: ")
        self.book=input()
        return self.book
     
class Lib(Library,User):

    library=Library(["Clean Code: By Robert C. Martin","The Pragmatic Programmer: Your Journey to Mastery","Code Complete","The Art of Computer Programming","Programming Pearls","Code:Charles Petzold","Introduction to Algorithms"])

    user=User()

    i=0
    while i==0:
            
        print("""****CHENNAI PUBLIC LIBRARY****
            1. Display the available books
            2. Borrow a book
            3. Return a book
            4. Donate a book
            5. Add user
            Press 0 to exit
            """)
        a=int(input("Enter your need:"))
        if a==1:
           library.disp()
        elif a==2:
           library.lendbook(user.BorrowBook())
        elif a==3:
           library.addbook1(user.ReturnBook())
        elif a==4:
           library.addbook2(user.DonateBook())
        elif a==5:
            user.adduser()
        elif a==0:
            exit()
        else:
      	   print("Please select the correct option")



               
                  
