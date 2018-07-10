class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("User email address updated!")

    def __repr__(self):
        return "User: {name} | Email: {email} | No. of books read: {books}".format(name = self.name, email = self.email, books = len(self.books.keys()) )

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            self = other_user

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        total_rating = 0
        rated_books = 0
        for i in self.books.values():
            if i is not None:
                total_rating += i
                rated_books += 1
        return (total_rating / rated_books)


class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("The ISBN was updated!")

    def add_rating(self, rating):
        try:
            if rating >= 0 and rating <= 4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")
        except:
            pass

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            self = other_book

    def get_average_rating(self):
        return sum(self.ratings)/len(self.ratings)

    def __repr__(self):
        return "{title}".format(title = self.title)

    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)



class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        b = Book(title, isbn)
        self.books[b] = 0
        return b


    def create_novel(self, title, author, isbn):
        n = Fiction(title, author, isbn)
        self.books[n] = 0
        return n


    def create_non_fiction(self, title, subject, level, isbn):
        nf = Non_Fiction(title, subject, level, isbn)
        self.books[nf] = 0
        return nf


    def add_book_to_user(self, book, email, rating = None):
        if self.users.get(email) is None:
            print("No user with email " + email)
        else:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] += 1

    def add_user(self, name, email, books = None):
        self.users[email] = User(name, email)
        if books is not None:
            for i in books:
                self.add_book_to_user(i, email, rating =  None)

    def print_catalog(self):
        for i in self.books.keys():
            print(i.title)

    def print_users(self):
        for i in self.users.keys():
            print(i)

    def most_read_book(self):
        value = 0
        most_read_book = ''
        for book, n in self.books.items():
            if n > value:
                most_read_book = book
                value = n
        return most_read_book

# extra method:
    def get_n_most_read_books(self, n):
      counter = 0
      sorted_books = sorted(self.books.items(), key=lambda x: x[1], reverse=True)
      print(str(n) + " most read books:")
      while counter < n:
        for i in range(n):
          print(str(i+1) + " | " + str(sorted_books[i]))
          counter += 1



    def highest_rated_book(self):
        highest_rating = float("-inf")
        highest_rated_book = ''
        for book in self.books.keys():
            if book.get_average_rating() > highest_rating:
                highest_rating = book.get_average_rating()
                highest_rated_book = book
        return highest_rated_book

    def most_positive_user(self):
        most_positive_user = ''
        highest_user_rating = float("-inf")
        for user in self.users.values():
            if user.get_average_rating() > highest_user_rating:
                highest_user_rating = user.get_average_rating()
                most_positive_user = user
        return most_positive_user
