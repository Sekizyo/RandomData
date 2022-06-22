import random

from engine.dateTimeGen import dateTimeGenerator
from engine.addressGen import addressGenerator

class personGenerator():
    def __init__(self):
        self.dateTimeGen = dateTimeGenerator()
        self.addressGen = addressGenerator()

    def getPersons(self, count=10):
        persons = []
        for _ in range(count):
            persons.append(self.getPerson())
        return persons

    def getPerson(self):
        person = {
            "firstname": self.firstName(),
            "lastname": self.lastName(),
            "gender": self.gender(),
            "nationality": self.nationality(),
            "age": self.age(),
            "birhtday": self.birthday(),
            "phone": self.phoneNr(),
            "email": self.email(),
            "address": self.address(),
            "website": self.website(),
            "image": self.image()
        }

        return person

    def firstName(self):
        firstNames = ["Maria", "Nushi", "Mohammed", "Jose", "Wei", "Yan", "David", "John", "Ana", "Michael"]
        return firstNames[random.randint(0, len(firstNames)-1)]

    def lastName(self):
        lastNames = ["Wang", "Smith", "Devi", "Ivanov", "Kim", "Ali", "Garcia", "Silva", "Hansen"]
        return lastNames[random.randint(0, len(lastNames)-1)]

    def gender(self):
        roll = random.randint(0, 2)
        if roll == 0:
            return "male"
        elif roll == 1:
            return "female"
        elif roll == 2:
            return "other"

    def nationality(self):
        nationalities = ["African", "Asian", "European", "Central American", "Middle Eastern", "North African", "South American", "Southeast Asian"]
        return nationalities[random.randint(0, len(nationalities)-1)]

    def age(self):
        return str(random.randint(0, 102))

    def birthday(self):
        return self.dateTimeGen.isoDate()

    def phoneNr(self):
        nr = ''
        nr += str(random.randint(6, 9))
        for i in range(1, 10):
            nr += str(random.randint(0, 9))
        return nr

    def email(self):
        return f"{self.firstName()}.{self.lastName()}@gmail.com"

    def address(self):
        return self.addressGen.getAddress()

    def website(self):
        return f"http://{self.firstName()}.{self.lastName()}.com"

    def image(self):
        return "http://placeimg.com/640/480/people"