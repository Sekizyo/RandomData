class placeGenerator():
    def latitude(self):
        return str(round(random.uniform(-90, 90), 7))
        
    def longitude(self):
        return str(round(random.uniform(-90, 90), 7))
