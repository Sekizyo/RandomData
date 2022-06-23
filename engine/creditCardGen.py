import random

from engine.utils import firstName, lastName

class creditCardGenerator():
    def getCreditCards(self, count=10):
        cards = []
        for _ in range(count):
            cards.append(self.getCreditCard())
        return cards

    def getCreditCard(self):
        card = {
            "type": self.company(),
            "number": self.number(),
            "expiration": self.expiration(),
            "ccv": self.ccv(),
            "owner": self.owner()
        }
        
        return card
        
    def company(self):
        companies = ["Visa", "MasterCard", "American Express", "Discover"]
        return companies[random.randint(0, len(companies)-1)]
        
    def number(self):
        return str(random.randint(1000000000000000, 9999999999999999))
        
    def expiration(self):
        year = str(random.randint(22, 99))

        month = str(random.randint(1, 12))
        if len(month) == 1:
            month = '0' + month

        return f"{month}/{year}"
    
    def ccv(self):
        return str(random.randint(100, 999))

    def owner(self):
        return f"{firstName()} {lastName()}"