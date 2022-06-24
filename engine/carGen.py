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
    
    def engine(self):
        return random.randfloat() #TODO check syntax

    def registration_nr(self):
        return

    def type_(self):
        types = ["Avansis", "Passat"]
        return types[random.randint(0, len(copmanies)-1)]

    def company(self):
        companies = ["Tesla", "Volvo", "Toyota", "Mercedes", "Alpha Romeo", "Audi", "Fiat"]
        return companies[random.randint(0, len(companies)-1)]

    def vin(self):
        return