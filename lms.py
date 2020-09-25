class Library:
    def __init__(self,listOfBooks):
        self.books=listOfBooks
    def displayAvailableBooks(self):
        print("Books present in this library are:")
        for book in self.books:
            print(book)
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName} return within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print(f"Sorry!This book is either not available or has already been issued to someone else")
            return False
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning the book")



        
class Student:
    def __init__(self):
        self.bookList=[]

    def  requestBook(self):
        self.book=input("Enter the name of the book you want to borrow ")
        return self.book
    def  returnBook(self):
        self.book=input("Enter the name of the book you want to return ")
        return self.book
        
if __name__ == "__main__":
    centralLibrary=Library(["CLRS","Django","Python","DennisRitchie"])
    student=Student()
    # centralLibrary.displayAvailableBooks()
    while True:
        welcomeMsg='''=======Welcome to Shivam Library Management System============
        Please choose an option:
        1.Listing all the books
        2.Request a book
        3.Add/Return a book
        4.Exit the Library'''
        print(welcomeMsg)
        a=int(input("Enter a choice"))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for choosing Shivam Library.Bye Bye")
            exit()
        else:
            print("Invalid Choice")

        
