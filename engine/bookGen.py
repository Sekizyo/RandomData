import random

from engine.personGen import personGenerator
from engine.dateTimeGen import dateTimeGenerator
class bookGenerator():
    def __init__(self):
        self.personGen = personGenerator()
        self.dateTimeGen = dateTimeGenerator()

    def getBooks(self, count=1):
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
            "isbn_10": self.isbn_10(),
            "isbn_13": self.isbn_13(),
            "ean": self.ean(),
            "image": self.image(),
            "published": self.published(),
            "publisher": self.publisher()
        }

        return book

    def title(self):
        titles = ["Gates of Dragons", "Secret of the Kissing Man", "The Groom in the West", "Forge and the Rose", "Sign of the Painted Fingernail", "His and Her Rules", "Throne and the Inferno", "Tapped for Sorrow"]
        return titles[random.randint(0, len(titles)-1)]

    def author(self):
        return f"{self.personGen.firstName()} {self.personGen.lastName()}"
        
    def genre(self):
        genre = ["Fantasy", "Sci-Fi", "Mystery", "Thriller", "Romance", "Westerns", "Dystopian", "Contemporary"]
        return genre[random.randint(0, len(genre)-1)]
        
    def description(self):
        descriptions = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean a volutpat lacus. Duis at tincidunt est, at venenatis erat. Sed quis sapien erat. Praesent sit amet nunc augue. Quisque suscipit interdum eros, sed facilisis libero aliquam vitae. Vestibulum blandit velit lacus, at accumsan urna finibus at. Morbi sed ipsum eget urna venenatis pretium at ac metus. Vestibulum in ante metus. Donec mollis leo non velit viverra, venenatis congue dolor viverra. Integer ac consequat nisl. Nullam in fringilla lacus, et placerat tortor. Aliquam hendrerit arcu vel urna mollis, sed fringilla mauris tincidunt. Etiam posuere condimentum nulla, et tincidunt tortor placerat at. Sed vulputate nisl eget sem egestas congue. Vestibulum dictum pellentesque felis, et lobortis sapien consectetur eu.", "Donec finibus lacus id urna placerat fringilla. Maecenas id ante vitae elit suscipit tristique sed in dolor. Sed consectetur pharetra accumsan. Donec aliquet justo pellentesque lectus lobortis ultrices. Duis urna turpis, iaculis in felis id, ultrices volutpat ipsum. Donec tortor arcu, luctus sit amet vulputate nec, accumsan nec mi. Nulla tempor enim tincidunt dui elementum, sed elementum nunc molestie. Quisque sit amet nisi a ante molestie scelerisque. Fusce eleifend nunc odio, vitae laoreet risus euismod suscipit. Etiam eget interdum enim. Vivamus tincidunt gravida lacus a ornare. Cras placerat nec nisi sed fermentum.", "Vestibulum tincidunt nunc sit amet molestie commodo. Nulla imperdiet sollicitudin sapien vitae aliquet. Curabitur euismod ante purus, imperdiet dapibus dolor tempor in. Proin vel volutpat ligula. Fusce faucibus libero a velit laoreet, eget tincidunt eros feugiat. Duis vestibulum consequat viverra. Etiam ultricies pharetra suscipit.", "Vestibulum tincidunt nunc sit amet molestie commodo. Nulla imperdiet sollicitudin sapien vitae aliquet. Curabitur euismod ante purus, imperdiet dapibus dolor tempor in. Proin vel volutpat ligula. Fusce faucibus libero a velit laoreet, eget tincidunt eros feugiat. Duis vestibulum consequat viverra. Etiam ultricies pharetra suscipit.", "Sed pulvinar nibh at augue molestie maximus. Nulla luctus mauris non faucibus dictum. Proin in tellus elit. Etiam nibh urna, sollicitudin consectetur viverra quis, egestas nec ex. Vivamus enim sem, placerat in ante nec, lobortis porttitor ex. Nullam volutpat eleifend consequat. Mauris vel sapien tristique, ullamcorper ligula a, tempor felis. Integer eu eros finibus, lacinia felis sed, fringilla tellus. Phasellus eget massa nec tellus faucibus efficitur et hendrerit ligula. Mauris egestas nulla sit amet neque mattis mollis. Ut quam turpis, ornare et porta eget, blandit in ligula. Donec gravida lorem at lorem tristique, a feugiat ex pulvinar. Pellentesque commodo a ante id tristique. Proin in nibh quis justo porta pretium sed ac felis. Curabitur hendrerit urna vitae venenatis euismod."]
        return descriptions[random.randint(0, len(descriptions)-1)]
    
    def ean(self):
        ean = ''
        for _ in range(13):
            ean += str(random.randint(0,9))
        return ean
        
    def isbn_10(self):
        isbn = ''
        for _ in range(7):
            isbn += str(random.randint(0,9))
        return f"978-{isbn[:5]}-{isbn[6]}"

    def isbn_13(self):
        isbn = ''
        for _ in range(10):
            isbn += str(random.randint(0,9))
        return f"978-{isbn[:8]}-{isbn[9]}"

    def image(self):
        return "https://placeimg.com/640/480/people"
        
    def published(self):
        return self.dateTimeGen.isoDate()
        
    def publisher(self):
        publishers = ["Hachette Book Group", "HarperCollins Publishers", "Macmillan Publishers", "Penguin Random House", "Simon & Schuster"]
        return publishers[random.randint(0, len(publishers)-1)]