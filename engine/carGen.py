import random

from engine.dateTimeGen import dateTimeGenerator
class carGenerator():
    def __init__(self):
        self.dateTimeGen = dateTimeGenerator()

    def getCars(self, count=10):
        cars = []
        for _ in range(count):
            cars.append(self.getCar())

        return cars

    def getCar(self):
        car = {
            "model": {
                "type": self.types(),
                "makes": self.makes(),
                "year": self.year(),
                "engine": {
                    "displacement": self.engineDisplacement(),
                    "configuration": self.engineConfiguration() 
                    }
            },
            "info":{
                "licence_plate": self.licence_plate(),
                "registration_nr": self.registration_nr(),
                "vin": self.vin()
            }
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

    def engineDisplacement(self):
        types = ["3.0 L", "3.6 L", "2.3 L", "6.2 L", "1.8 L", "1.9 L"]
        return types[random.randint(0, len(types)-1)]

    def engineConfiguration(self):
        types = ["Straight-six", "Straight-four", "V6", "V8", "V10"]
        return types[random.randint(0, len(types)-1)]

    def types(self):
        types = ["SUV", "Sedan", "Coupe, Conv", "Pickup", "Van/Minivan", "Convertible", "Hatchback, ", "Hatchback", "Coupe", "Sedan"]
        return types[random.randint(0, len(types)-1)]

    def makes(self):
        companies =["Audi", "Chevrolet", "Cadillac", "Acura", "BMW", "Chrysler", "Ford", "Buick", "INFINITI", "GMC", "Honda", "Hyundai", "Jeep", "Genesis", "Dodge", "Jaguar", "Kia", "Land Rover", "Lexus", "Mercedes-Be", "Mitsubishi", "Lincoln", "MAZDA", "Nissan", "MINI", "Porsche", "Ram", "Subaru", "Toyota", "Volkswagen", "Volvo", "Alfa Romeo", "FIAT", "Freightline", "Maserati", "Tesla", "Aston Marti", "Bentley", "Ferrari", "Lamborghini", "Lotus", "McLaren", "Rolls-Royce", "smart", "Scion", "SRT", "Suzuki", "Fisker", "Maybach", "Mercury", "Saab", "HUMMER", "Pontiac", "Saturn", "Isuzu", "Panoz", "Oldsmobile", "Daewoo", "Plymouth", "Eagle", "Geo", "Daihatsu"]
        return companies[random.randint(0, len(companies)-1)]
    
    def year(self):
        return self.dateTimeGen.isoDate()["year"]

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