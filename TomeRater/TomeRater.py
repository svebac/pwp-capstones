class User(object):
    #Constructor of class User
    def __init__(self, name, email):
        #name will be a string
        self.name = name
        #email will be a string
        self.email = email
        #books is a dictionary
        self.books = {}
    #Returns Name and eMail of User
    def __repr__(self):
        return ("User " + self.name + ", email: " + self.email + ", books read: " + str(len(self.books)))
    #Returns True, if User and other user are equal, otherwise False
    def __eq__(self, other_user):
        if (self.name == other_user.name) and (self.email == other_user.email):
            return True
        else:
            return False
    #Method get_email will return eMail of User
    def get_email(self):
        return self.email
    #Method change_email will change eMail of User
    def change_email(self, address):
        self.email = address
        print("eMail of user has been updated!")
    #read book and rate book
    def read_book(self,book,rating = None):
        self.books[book] = rating
    #calculate average rating of books
    def get_average_rating(self):
        average = 0.0
        summary = 0
        i = 0
        for rating in self.books.values():
            if rating is not None:
                summary += rating
                i += 1
        if i > 0:
            average = float(summary / i)
        return average
        
class Book(object):
    def __init__(self,title,isbn):
        #Title of Book will be a string
        self.title = title
        #ISBN of book will be a number
        self.isbn = isbn
        #ratins will be a list
        self.ratings = []
    #__repr__ will return representation string
    def __repr__(self):
       	return (self.title + " with ISBN " + str(self.isbn))		
	#__eq__ compare isbn and title of two books
    def __eq__(self,other_book):
        if(self. title == other_book.title) and (self.isbn == other_book.isbn):
            return True
        else:
            return False
    #is object hashable or not?!    
    def __hash__(self):
        return hash((self.title, self.isbn))
    #get_title returns title of the book
    def get_title(self):
        return self.title
    #get_isbn returns isbn of the book
    def get_isbn(self):
        return self.isbn
    #set_isbn sets the isbn of the book to new_isbn
    def set_isbn(self,new_isbn):
        self.isbn = new_isbn
        print("The isbn of this book has been updated!")
    #Method add_rating adds a rating to tatings list, if rating is valid
    def add_rating(self,rating):
        if (rating >= 0) and (rating <= 4):
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
    def get_average_rating(self):
        average = 0.0
        summary = 0
        i = 0
        for rating in self.ratings:
            summary += rating
            i += 1
        average = float(summary / i)
        return average    
#class Fiction represents as subclass from book all Fiction Books        
class Fiction(Book):
    #Contructor call first parent __init__
    def __init__(self,title,author,isbn):
        Book.__init__(self,title,isbn)
        self.author = author
    #__repr__ will return representation string
    def __repr__(self):
        return (self.title + " by " + self.author)
    #get_author returns the author
    def get_author(self):
        return self.author
    
#class Non_Fiction represents as subclass from book all Non_Fiction Books 
class Non_Fiction(Book):
    #Contructor call first parent __init__
    def __init__(self,title,subject,level,isbn):
        Book.__init__(self,title,isbn)
        #subject will be a string
        self.subject = subject
        #level will be a string
        self.level = level
    #__repr__ will return representation string
    def __repr__(self):
        return (self.title + ", a " + self.level + " manual on " + self.subject)
    #get_subject returns the subject
    def get_subject(self):
        return self.subject
    #get_level returns the level
    def get_level(self):
        return self.level
        
#Class TomeRater
class TomeRater():
    #__init__
    def __init__(self):
        #This dictionary will map a users email to the corresponding user object
        self.users ={}
        #This dictionary will map a book object to the number of Users that have read it
        self.books = {}
    #This method creates a new Book
    def create_book(self,title,isbn):
        return Book(title,isbn)
    #This method creates a new novel
    def create_novel(self,title,author,isbn):
        return Fiction(title,author,isbn)
    #this method creates a new Non_fiction
    def create_non_fiction(self,title,subject,level,isbn):
        return Non_Fiction(title,subject,level,isbn)
    def check_isbn(self, book):
        for key in self.books.keys():
            if key.get_isbn() == book.get_isbn():
                if key.get_title() != book.get_title():
                    print("ISBN already exists!")
                    return False
        return True  
    #This method adds a book to a user
    def add_book_to_user(self,book,email,rating = None):
        print("in add book: " + book.title + " to user: " + email)
        #check if user exists in TomeRater
        if email in self.users.keys():
            #check if isbn already exists in users books
            if self.check_isbn(book):
                self.users[email].read_book(book,rating)
            if rating is not None:
                book.add_rating(rating)
                if book not in self.books:
                    self.books[book] = 1
                else:
                    self.books[book] += 1
        else:
            print("No user with email " + email)
            
    #This method adds a user to Tomerater
    def add_user(self,name,email,user_books = None):
        #check if email-address is valid
        if ("@" in email) and ((".org" in email) or (".edu" in email) or (".com" in email)):
            #check if user already exists
            if email in self.users:
                print("User alredy exists!")
            else:
                self.users[email] = User(name,email) 
                if user_books is not None:
                    for book in user_books:
                        self.add_book_to_user(book,email)
        else:
            print("Email-address is not valid!")
    #iterates through self.books and prints them
    def print_catalog(self):
        for key in self.books.keys():
            print(key)
    #iterates trough all of the values of self.users and prints them
    def print_users(self):
        for item in self.users.items():
            print(item)
    #iterates through all of the books in self.books and return most popular one
    def most_read_book(self):
        ret_book = ""
        act_val = 0
        for item in self.books.items():
            if item.values() > act_val:
                ret_book = item.keys()
        return ret_book
    #Return highest rated book
    def highest_rated_book(self):
        ret_book = ""
        av_rating = 0
        for book in self.books.keys():
            if book.get_average_rating() > av_rating:
                av_rating = book.get_average_rating()
                ret_book = book
        return ret_book
    #Return most positive user
    def most_positive_user(self):
        ret_user = ""
        av_rating = 0
        for user in self.users.values():
            if user.get_average_rating() > av_rating:
                av_rating = user.get_average_rating()
                ret_user = user
        return ret_user
            
            
#Test class User
#test_object_User = User("Karl Dall", "karl.dall@gmail.com")
#print(test_object_User)
#Test class Fiction
#test_object_Fiction = Fiction("Das Boot","Lothar Günther Buchheim",12345)
#print(test_object_Fiction)
#Test class Non_Fiction
#test_object_Non_Fiction = Non_Fiction("Society of mind","Artificial intelligence","beginner",12346)
#print(test_object_Non_Fiction)
#Test class Tome rater
#test_tomerater = TomeRater()
#test_tomerater.add_book_to_user("Frankenstein","karl.dall@gmail.com",3)
#print(test_object_User)
#print(books)
