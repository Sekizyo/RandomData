import random

from engine.personGen import personGenerator
from engine.dateTimeGen import dateTimeGenerator
class bookGenerator(): #TODO add content
    def __init__(self):
        self.personGen = personGenerator()
        self.dateTimeGen = dateTimeGenerator()

    def getBooks(self, count=10):
        books = []
        for _ in range(count):
            books.append(self.getBook())
        return books

    def getBook(self):
        book = {
            "title": self.title(),
            "author": self.author(),
            "genre": self.genre(),
            "description": self.description(),
            "isbn": self.isbin(),
            "image": self.image(),
            "published": self.published(),
            "publisher": self.publisher()
        }

        return book

    def title(self):
        titles = []
        return titles[random.randomint(0, len(titles)-1)]

    def author(self):
        authors = []
        return authors[random.randomint(0, len(authors)-1)]
        
    def genre(self):
        genre = []
        return genre[random.randomint(0, len(genre)-1)]
        
    def description(self):
        descriptions = []
        return descriptions[random.randomint(0, len(descriptions)-1)]
        
    def isbn(self): #TODO add isbn
        pass

    def image(self):
        return "http://placeimg.com/640/480/book"
        
    def published(self):
        return self.dateTimeGen.isoDate()
        
    def publisher(self):
        publishers = []
        return publishers[random.randomint(0, len(publishers)-1)]