import random

from engine.personGen import personGenerator

class userGenerator():
    def __init__(self):
        self.personGen = personGenerator()

    def getUsers(self, count=10):
        users = []
        for _ in range(count):
            users.append(self.getUser())

        return users

    def getUser(self):
        user = {
            "uuid": self.uuid(),
            "firstname": self.firstName(),
            "lastname": self.lastName(),
            "username": self.username(),
            "password": self.password(),
            "email": self.email(),
            "ip": self.ip(),
            "macAddress": self.macAddress(),
            "website": self.website(),
            "image": self.image(),
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
        uuid += random.choice("-")

        return uuid
        
    def firstName(self):
        return self.personGen.firstName()
        
    def lastName(self):
        return self.personGen.lastName()

    def username(self):
        return f"{self.firstName()}.{self.lastName()}{random.randint(0, 1000)}"
        
    def password(self):
        return f"{self.firstName()}.{self.lastName()}{random.randint(0, 1000)}"
        
    def email(self):
        return f"{self.firstName()}.{self.lastName()}@gmail.com"

    def ip(self):
        return f"{random.randint(120, 196)}.{random.randint(100, 254)}.{random.randint(10, 196)}.{random.randint(10, 254)}"

    def macAddress(self):
        address = ""
        for _ in range(6):
            address += random.choice("123456789ABCDEF")
            address += random.choice("123456789ABCDEF")
            address += random.choice(":")
        return address
        
    def website(self):
        return self.personGen.website()

    def image(self):
        return self.personGen.image()