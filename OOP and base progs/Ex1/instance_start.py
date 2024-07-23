class Book:
    def __init__(self,title,author,pages,price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attr"

    def getPrice(self):
        if hasattr(self,"_discount"):
            return self.price-(self.price*self._discount)
        else:
            return self.price

    def setdiscounts(self,amount):
        self._discount=amount

book1 = Book("Brave new World","JD Salinger",234,29.95)
book2 = Book("War and Peace", "Leo Tolstoy",1225,39.95)

print(book1.title)
print(book1.getPrice())
book1.setdiscounts(0.25)
print(book1.title)
print(book1.getPrice())


#secret
print(book1._Book__secret)