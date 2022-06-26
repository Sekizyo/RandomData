import random

from engine.dateTimeGen import dateTimeGenerator
from engine.addressGen import addressGenerator
from engine.creditCardGen import creditCardGenerator
from engine.carGen import carGenerator

class personGenerator():
    def __init__(self):
        self.dateTimeGen = dateTimeGenerator()
        self.addressGen = addressGenerator()
        self.creditCardGen = creditCardGenerator()
        self.carGen = carGenerator()

    def getPersons(self, count=10):
        persons = []
        for _ in range(count):
            persons.append(self.getPerson())
        return persons

    def getPerson(self):
        gender = self.gender()
        firstName = self.firstName(gender)
        lastName = self.lastName()

        person = {
            "name": {
                "title": self.title(gender),
                "firstname": firstName,
                "lastname": lastName
            },
            "gender": gender,
            "nationality": self.nationality(),
            "date of birth": {
                "age": self.age(),
                "birthday": self.birthday(),
            },
            "contact": {
                "phone": self.phoneNr(),
                "email": self.email(firstName, lastName)
            },
            "address": self.address(),
            "website": self.website(firstName, lastName),
            "image": self.image(gender),
            "payment": {
                "credit_card": self.creditCard(firstName, lastName),
                "bitcoin": self.bitcoin()
            },
            "car": self.carGen.getCar()
        }

        return person

    def title(self, gender):
        if gender == "male":
            return "Mr"
        elif gender == "female":
            return "Mrs"
        else:
            return "Mx"

    def firstName(self, gender):
        males = []#TODO
        females = []
        other = []

        firstNames = ["Maria", "Nushi", "Mohammed", "Jose", "Wei", "Yan", "David", "John", "Ana", "Michael"]
        return firstNames[random.randint(0, len(firstNames)-1)]

    def lastName(self):
        lastNames = ["Wang", "Smith", "Devi", "Ivanov", "Kim", "Ali", "Garcia", "Silva", "Hansen"]
        return lastNames[random.randint(0, len(lastNames)-1)]

    def gender(self):
        return random.choice(["male", "female", "other"])

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

    def email(self, firstName, lastName):
        return f"{firstName}.{lastName}@gmail.com"

    def address(self):
        return self.addressGen.getAddress()

    def website(self, firstName, lastName):
        return f"http://{firstName}.{lastName}.com"

    def image(self, gender):
        imageNr = random.randint(1, 99)
        if gender == "other":
            gender = random.choice(["male", "female"])
        return {"large":f"https://randomuser.me/api/portraits/{gender}/{imageNr}.jpg", "medium": f"https://randomuser.me/api/portraits/med/{gender}/{imageNr}.jpg", "thumbnail": f"https://randomuser.me/api/portraits/thumb/{gender}/{imageNr}.jpg"}

    def creditCard(self, firstName, lastName):
        return self.creditCardGen.getCreditCard(f"{firstName} {lastName}")

    def bitcoin(self):
        wallet = ""
        chars = "123456789acdefghjklmnprstwxz"
        wallet += str(random.randint(1, 3))
        lenght = random.randint(26, 34)

        for _ in range(lenght):
            wallet += random.choice(chars)

        return wallet

