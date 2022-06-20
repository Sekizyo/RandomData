import random 

class placeGenerator():
    def getPlaces(self, count=10):
        places = []
        for _ in range(count):
            places.append(self.getPlace())

        return places

    def getPlace(self):
        place = {
            "latitude": self.latitude(),
            "longitude": self.longitude()
        }

        return place

    def latitude(self):
        return str(round(random.uniform(-90, 90), 7))
        
    def longitude(self):
        return str(round(random.uniform(-90, 90), 7))
