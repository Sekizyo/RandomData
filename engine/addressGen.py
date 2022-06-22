import random

class addressGenerator():
    def getAddresses(self, count=10):
        addresses = []
        for _ in range(count):
            addresses.append(self.getAddress())
        return addresses

    def getAddress(self):
        address = {
            "streetname": self.streetName(),
            "country": self.country(),
            "countryCode": self.countryCode(),
            "city": self.city(),
            "zipcode": self.zipCode(),
            "buildingnumber": self.buildingNumber(),
            "latitude": self.latitude(),
            "longitude": self.longitude(),

        }
        
        return address

    def streetName(self):
        streetNames = ["Austin Garth", "Appleby Square", "Armstrong Parkway", "Appletree Circle", "Archer Gate", "Allmains Close", "Ainsdale Boulevard", " Alissa Drive", "Allen Wharf", "Artington Close"]
        return streetNames[random.randint(0, len(streetNames)-1)]

    def country(self):
        countries = ["Australia", "Poland", "Germany", "France", "Austria", "India", "Brazil", "China", "Denmark", "Egypt", "Finland", "Italy", "Lithuenia", "United States of America"]
        return countries[random.randint(0, len(countries)-1)]

    def countryCode(self):
        code = str(random.randint(1000, 1500))
        if len(code) == 4:
            code = code[:1] + '-' + code[1:]
        return code

    def city(self):
        cityies = ["Tokyo", "Delhi", "Shanghai", "Sao Paulo", "Mexico City", "Beijing", "Mumbai", "Osaka", "Dhaka", "Cairo", "Karchi", "Paris", "Warsaw", "Berlin", "Prague", "BUdapest", "Madrit"]
        return cityies[random.randint(0, len(cityies)-1)]

    def zipCode(self):
        return f"{random.randint(0, 9)}{random.randint(0, 99)}{random.randint(0, 99)}"

    def buildingNumber(self):
        return str(random.randint(0, 1000))

    def latitude(self):
        return str(round(random.uniform(-90, 90), 7))
        
    def longitude(self):
        return str(round(random.uniform(-90, 90), 7))
