class textGenerator():
    def getTexts(self, count=10):
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
        pass

    def author(self):
        pass
        
    def genre(self):
        pass
        
    def content(self):
        pass