import random
class carGenerator():
    def getCars(self, count=10):
        cars = []
        for _ in range(count):
            cars.append(self.getCar())

        return cars

    def getCar(self):
        car = {
            "licence_plate": self.licence_plate(),
            "registration_nr": self.registration_nr(),
            "engine": self.engine(),
            "type": self.type_(),
            "company": self.company(),
            "vin": self.vin()
        }

        return car

    def licence_plate(self):
        areaCodes = ["BSE", "BS"]
        code = areaCodes[random.randint(0, len(areaCodes)-1)]

        chars = "123456789ABCDEFGHIMNOPXZ"
        nr = ""
        for _ in range(5):
            nr += random.choice(chars)

        return f"{code} {nr}"
    

    def registration_nr(self):
        return

    def engine(self):
        types = ["V6"]
        # return random.randfloat() #TODO check syntax
        return

    def type_(self):
        types = ["Avansis", "Passat"]
        return types[random.randint(0, len(types)-1)]

    def company(self):
        companies = ["Tesla", "Volvo", "Toyota", "Mercedes", "Alpha Romeo", "Audi", "Fiat"]
        return companies[random.randint(0, len(companies)-1)]

    def vin(self):
        vin = ""
        chars = "ABCDEFGHIMNOPXZ"
        charsNumbers= "123456789ABCDEFGHIJKMNOPWZX"
        vin += str(random.randint(1, 9))
        for _ in range(2):
            vin += random.choice(chars)
        
        for _ in range(5):
            vin += random.choice(charsNumbers)
        
        for _ in range(3):
            vin += random.choice(chars)

        vin += str(random.randint(100000, 999999))
        return