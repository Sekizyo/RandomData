import random

from engine.personGen import personGenerator

class textGenerator():
    def __init__(self):
        self.personGen = personGenerator()

    def getTexts(self, count=1):
        texts = []
        for _ in range(count):
            texts.append(self.getText())
        
        return texts

    def getText(self):
        text = {
            "title": self.title(),
            "author": self.author(),
            "genre": self.genre(),
            "content": self.content()
        }
        
        return text
        
    def title(self):
        titles = ["Gates of Dragons", "Secret of the Kissing Man", "The Groom in the West", "Forge and the Rose", "Sign of the Painted Fingernail", "His and Her Rules", "Throne and the Inferno", "Tapped for Sorrow"]
        return titles[random.randint(0, len(titles)-1)]

    def author(self):
        firstname = self.personGen.firstName()
        lastname = self.personGen.lastName()

        return f"{firstname} {lastname}"
        
    def genre(self):
        genre = ["Crime", "Fantasy", "Mystery", "Romance", "Sci-fi"]
        return genre[random.randint(0, len(genre)-1)]
        
    def content(self):
        content = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean a volutpat lacus. Duis at tincidunt est, at venenatis erat. Sed quis sapien erat. Praesent sit amet nunc augue. Quisque suscipit interdum eros, sed facilisis libero aliquam vitae. Vestibulum blandit velit lacus, at accumsan urna finibus at. Morbi sed ipsum eget urna venenatis pretium at ac metus. Vestibulum in ante metus. Donec mollis leo non velit viverra, venenatis congue dolor viverra. Integer ac consequat nisl. Nullam in fringilla lacus, et placerat tortor. Aliquam hendrerit arcu vel urna mollis, sed fringilla mauris tincidunt. Etiam posuere condimentum nulla, et tincidunt tortor placerat at. Sed vulputate nisl eget sem egestas congue. Vestibulum dictum pellentesque felis, et lobortis sapien consectetur eu.", "Donec finibus lacus id urna placerat fringilla. Maecenas id ante vitae elit suscipit tristique sed in dolor. Sed consectetur pharetra accumsan. Donec aliquet justo pellentesque lectus lobortis ultrices. Duis urna turpis, iaculis in felis id, ultrices volutpat ipsum. Donec tortor arcu, luctus sit amet vulputate nec, accumsan nec mi. Nulla tempor enim tincidunt dui elementum, sed elementum nunc molestie. Quisque sit amet nisi a ante molestie scelerisque. Fusce eleifend nunc odio, vitae laoreet risus euismod suscipit. Etiam eget interdum enim. Vivamus tincidunt gravida lacus a ornare. Cras placerat nec nisi sed fermentum.", "Vestibulum tincidunt nunc sit amet molestie commodo. Nulla imperdiet sollicitudin sapien vitae aliquet. Curabitur euismod ante purus, imperdiet dapibus dolor tempor in. Proin vel volutpat ligula. Fusce faucibus libero a velit laoreet, eget tincidunt eros feugiat. Duis vestibulum consequat viverra. Etiam ultricies pharetra suscipit.", "Vestibulum tincidunt nunc sit amet molestie commodo. Nulla imperdiet sollicitudin sapien vitae aliquet. Curabitur euismod ante purus, imperdiet dapibus dolor tempor in. Proin vel volutpat ligula. Fusce faucibus libero a velit laoreet, eget tincidunt eros feugiat. Duis vestibulum consequat viverra. Etiam ultricies pharetra suscipit.", "Sed pulvinar nibh at augue molestie maximus. Nulla luctus mauris non faucibus dictum. Proin in tellus elit. Etiam nibh urna, sollicitudin consectetur viverra quis, egestas nec ex. Vivamus enim sem, placerat in ante nec, lobortis porttitor ex. Nullam volutpat eleifend consequat. Mauris vel sapien tristique, ullamcorper ligula a, tempor felis. Integer eu eros finibus, lacinia felis sed, fringilla tellus. Phasellus eget massa nec tellus faucibus efficitur et hendrerit ligula. Mauris egestas nulla sit amet neque mattis mollis. Ut quam turpis, ornare et porta eget, blandit in ligula. Donec gravida lorem at lorem tristique, a feugiat ex pulvinar. Pellentesque commodo a ante id tristique. Proin in nibh quis justo porta pretium sed ac felis. Curabitur hendrerit urna vitae venenatis euismod."]
        return content[random.randint(0, len(content)-1)]