from Users import Users
from Book import Book


class Libraray:
    
     def __init__(self):
        self.books = []
        self.Users = []
     def add_book(self, book):
        self.books.append(book)
     def remove_book(self, book):
            if book in self.books:
               self.books.remove(book)
            else:
               print("Book not found in the library.")
     def display_books(self):
            print("Available Books:")
            for book in self.books:
                print(book)
     def add_user(self ,user):
         self.Users.append(user)
     def remove_User (self ,user):
         if user in self.Users:
            self.Users.remove(user)
         else:
             print ("No User With THis Name")
     def dispaly_user (self):
         print("Users:")
         for user in self.Users:
             print (user)
           
lib =Libraray()
book1 = Book("Python ", "John Smith" ,"this book for beginners ")
book2 = Book("c# ", "issam " ,"this book for beginners ")
lib.add_book(book1);
lib.add_book(book2);

lib.display_books();


User1 = Users("Aya ","25","maadi","aya@gmail.com")
User2 = Users("hala ","25","dokki","hala@gmail.com")
lib.add_book(User1);
lib.add_book(User2);

lib.dispaly_user();

  