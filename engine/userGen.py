import random
import hashlib

from engine.personGen import personGenerator
from engine.dateTimeGen import dateTimeGenerator

class userGenerator():
    def __init__(self):
        self.personGen = personGenerator()
        self.dateTimeGen = dateTimeGenerator()

    def getUsers(self, count=1):
        users = []
        for _ in range(count):
            users.append(self.getUser())

        return users

    def getUser(self):
        firstName = self.firstName()
        lastName = self.lastName()

        user = {
            "uuid": self.uuid(),
            "firstname": firstName,
            "lastname": lastName,
            "username": self.username(),
            "password": self.password(),
            "md5_password": self.md5_password(),
            "email": self.email(),
            "ip": self.ip(),
            "macAddress": self.macAddress(),
            "website": self.website(firstName, lastName),
            "image": self.image(),
            "registered": self.dateTimeGen.isoDateTime()
        }
        
        return user

    def uuid(self):
        uuid = ""
        chars = "123456789ABCDEF"
        for _ in range(8):
            uuid += random.choice(chars)
        uuid += random.choice("-")

        for _ in range(4):
            uuid += random.choice(chars)
        uuid += random.choice("-")
        
        for _ in range(4):
            uuid += random.choice(chars)
        uuid += random.choice("-")

        for _ in range(4):
            uuid += random.choice(chars)
        uuid += random.choice("-")

        for _ in range(12):
            uuid += random.choice(chars)

        return uuid
        
    def firstName(self):
        return self.personGen.firstName()
        
    def lastName(self):
        return self.personGen.lastName()

    def username(self):
        return f"{self.firstName()}.{self.lastName()}{random.randint(0, 1000)}"
        
    def password(self):
        return f"{self.firstName()}.{self.lastName()}{random.randint(0, 1000)}"

    def md5_password(self):
        return hashlib.md5(self.password().encode('utf-8')).hexdigest()
        
    def email(self):
        return f"{self.firstName()}.{self.lastName()}@gmail.com"

    def ip(self):
        return f"{random.randint(120, 196)}.{random.randint(100, 254)}.{random.randint(10, 196)}.{random.randint(10, 254)}"

    def macAddress(self):
        address = ""
        chars = "123456789ABCDEF"
        for _ in range(6):
            address += random.choice(chars)
            address += random.choice(chars)
            address += ":"
        return address
        
    def website(self, firstName, lastName):
        return self.personGen.website(firstName, lastName)

    def image(self):
        return self.personGen.image()
