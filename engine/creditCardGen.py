import random

from engine.utils import firstName, lastName
from engine.dateTimeGen import dateTimeGenerator


class creditCardGenerator():
    def __init__(self):
        self.date = dateTimeGenerator()

    def getCreditCards(self, count=1):
        cards = []
        for _ in range(count):
            cards.append(self.getCreditCard(f"{firstName()} {lastName()}"))
        return cards

    def getCreditCard(self, owner=f"{firstName()} {lastName()}"):
        card = {
            "type": self.company(),
            "number": self.number(),
            "expiration": self.expiration(),
            "ccv": self.ccv(),
            "owner": owner
        }
        
        return card

    def getCCTransactions(self, count=5):
        transactions = []
        for _ in range(count):
            transactions.append(self.getCCTransaction())
        return self.sortTransactions(transactions)

    def sortTransactions(self, trns):
        return sorted(trns, key=lambda d: d["date"])

    def getCCTransaction(self):
        transaction = {
            "cc_number": self.number(),
            "date": self.date.isoDateToday(),
            "type": self.transactionType(),
            "amount": self.amount()
        }

        return transaction
        
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
    
    def transactionType(self):
        types = ["ATM deposit", "ATM withdraw", "Charge", "Deposit", "Online withdraw", "Transfer"]
        return types[random.randint(0, len(types)-1)]

    def amount(self):
        return str(round(random.uniform(1, 10000), 2))

