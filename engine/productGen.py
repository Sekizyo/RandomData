import random

class productGenerator():
    def getProducts(self, count=10):
        products = []
        for _ in range(count):
            products.append(self.getProduct())
        
        return products

    def getProduct(self):
        productName = self.name()
        product = {
            "name": productName,
            "description": self.description(productName),
            "ean": self.ean(),
            "upc": self.upc(),
            "image": self.image(),
            "price": self.price(),
            "netprice": self.netPrice(),
            "taxes": self.taxes(),
            "category": self.category(),
        }
        
        return product
        
    def name(self):
        names = ["Bike","Bik","The Best Bike","Organic Bike","Bike for the Times","Bike for All","Bike of the People","Bike That Rock","Bike-izer","Bike-ak","I Can't Believe It's Not Bike!","Bike Smack","Sneaky Bike","The Sneaky Bike", "The Best Red Wine", "Organic Red Wine", "Red Wine for the Times", "Red Wine for All", "Red Wine of the People", "Red Wine That Rock", "Red Wine-izer", "Red Wine-ak", "I Can't Believe It's Not Red Wine!", "Red Wine Smack", "Sneaky Red Wine", "The Sneaky Red Wine", "That Red Wine Time", "Red Wine-alyzer", "Red Wine Gun", "Red Wine Kaboom", "The Red Wine Project", "Pop Red Wine", "Red Wine Pop", "Red Wine Aid", "Red Wine Hoop", "Red Wine Wrap", "Red Wine-ophane", "Red Wine-oin", "Red Wine App", "Red Wine Tone", "Red Wine-yo", "Zip Red Wine", "Red Wine Chain", "Red Wine Helper", "The Red Wine Helper", "Red Wine Storage", "Max Red Wine", "Red Wine to the Max", "Red Wine-o-pot", "Red Wine-ex", "Red Wine-aphone", "Red Wine-mobile", "Red Wine-uzzi", "Red Wine Stick", "Red Wine Tape", "Red Wine Hero", "Red Wine Knife", "Red Wine-enol", "Red Wine Man", "Red Wine Woman", "Red Wine Dog", "Red Wine Dude", "Red Wine Ex", "Red Wine Bay", "Red Wine Apparel", "Red Wine Care", "Red Wine Luxury", "Red Wine Automotive", "The Personal Red Wine", "Red Wine Insurance", "Red Wine Food", "Red Wine Nutrition", "Red Wine Supplements", "Red Wine Medicine", "Red Wine Beer", "Red Wine Fast", "Fast Red Wine", "Red Wine Provider", "Red Wine Retail", "Red Wine Alliance", "The Red Wine Alliance", "Red Wine-pac", "Red Wine Mart", "Soft Red Wine", "Hard Red Wine", "Fast Red Wine", "Red Wine Bank", "Red Wine Video", "Red Wine Wrap", "Super Red Wine", "Post Red Wine", "Red Wine Buster", "Red Wine Pad", "Red Wine Pep", "Crazy Red Wine", "Red Wine Book", "Red Wine Company", "Red Wine Brand", "Red Wine Carta", "Red Wine Card", "The Worst Red Wine", "The Best Red Wine", "World's Okayest Red Wine", "OK Red Wine", "Okay Red Wine", "Hello Red Wine", "Fresh Red Wine", "Red Wine X", "Crypto Red Wine", "Anti-Red Wine", "The Red Wine Movement", "Red Wine Movement", "Rise Red Wine", "Shiny Red Wine", "Dumb Red Wine", "Single Red Wine", "Red Wine Serve", "Red Wine-soft", "Tame Red Wine", "Master Red Wine", "Red Wine Type", "Super Duper Red Wine", "Spectacular Red Wine", "Amazing Red Wine", "Red Wine Away", "Red Wine BnB", "Red Wine Hotel", "Red Wine Scout", "The Red Wine Project", "Red Wine Fix", "Fix Red Wine", "Red Wine Corporation", "Red Wine Media", "Red Wine Turf", "Red Wine Cash", "Red Wine Stick", "Chuck Red Wine", "Red Wine-it", "iRed Wine", "Red Wine Beep", "Red Wine Electronics", "Red Wine Electrical", "Red Wine Start", "Starter Red Wine", "Red Wine Box", "Box-o-Red Wine", "Red Wine Reality", "The Red Wine Experience", "Time to Red Wine", "It's Not Even Red Wine", "Way to Red Wine", "Red Wine Band", "Red Wine Garage", "Red Wine Cream", "Ice Red Wine", "Better Red Wine", "Red Wine Mint", "Red Wine Bowl", "Manly Red Wine", "Tourist Red Wine", "Red Wine Tour", "Red Wine Car", "Red Wine-O", "Red Wine-atron", "Red Wine Chronicles", "Red Wine Pocket", "Pocket of Red Wine", "Red Wine Limited", "Red Wine Edition", "Red Wine Ski", "Scoop of Red Wine", "Red Wine Woo", "Awesome Red Wine", "Amazing Red Wine", "Wondrous Red Wine", "Wonder Red Wine", "Red Wine Perfume", "Red Wine Scent", "Red Wine Cologne", "Red Wine Bag", "Red Wine Furniture", "Just for Red Wine", "InstaRed Wine", "Instant Red Wine", "Immediate Red Wine", "Red Wine Right Now", "Red Wine Forever", "Forever Red Wine", "Insane Red Wine", "Red Wine Insanity", "Red Wine Creame", "Creme-de-Red Wine", "Red Wine Lotion", "Red Wine Butter", "Red Wine Food", "Foodie Red Wine", "Red Wine Ball", "Red Wine Pump", "Red Wine Scope", "Prisma Red Wine", "American Red Wine", "European Red Wine", "Asian Red Wine", "Brazilian Red Wine", "Canadian Red Wine", "The Red Wine Concept", "The Red Wine Book", "Concept Red Wine", "Future Red Wine", "White Red Wine", "Black Red Wine", "Red Red Wine", "Red Wine Snake", "Red Wine Bottle", "Watch Me Red Wine", "Get Your Red Wine On", "Red Wine Credit", "Red Wine Kiss", "Kiss of Red Wine", "Red Wine Store", "Red Wine In a Box", "Red Wine In a Bottle", "Red Wine Rabbit", "Task Red Wine", "Red Wine Milk", "Canned Red Wine", "Pass the Red Wine", "Red Wine 77", "1st Place Red Wine", "2nd Place Red Wine", "No Place Like Red Wine", "There's Nothing Like Red Wine", "It's a Red Wine!", "Don't Have a Red Wine", "Famous Red Wine", "Top Red Wine", "Cruelty Free Red Wine", "Vegan Red Wine", "Meat Easter's Red Wine", "The Champagne of Red Wine", "Red Wine Wine", "Red Wine Bracelet", "Red Wine Partners", "Wife's Red Wine", "Husband's Red Wine", "Kids Red Wine", "Red Wine for Kids", "Red Wine Business", "Red Wine 9000", "Not Your Grandmothers Red Wine", "Red Wine Calendar", "Red Wine Wrap", "Wrapped Red Wine", "Red Wine CK", "Red Wine Logo", "Red Wine Label", "Red Wine Shoe", "Badass Red Wine", "Off the Wall Red Wine", "Red Wine Pills", "Red Wine Tube", "Red Wine Gloss", "Swag Red Wine", "Red Wine Tablet", "Red Wine Phone", "Modular Red Wine", "Red Wine Strap", "Red Wine Ride", "Red Wine Size", "Red Wine Drive", "Yellow Red Wine", "Smart Red Wine", "Red Wine Smart", "Today Red Wine", "Popular Red Wine", "Celebrity Red Wine", "Fine Red Wine", "Red Wine Shoulder", "Red Wine Allergy", "Red Wine Clean", "Clean Red Wine", "Silky Red Wine", "Baby Red Wine", "Auto Red Wine", "Call of Red Wine", "Red Wine Spread", "Red Wine Knoll", "RX Red Wine", "Red Wine Tool", "Red Wine Smile", "Family Red Wine", "Red Wine Reality", "Chocolate Red Wine", "Naked Red Wine", "Red Wine Juice", "Freedom Red Wine", "Red Wine Square", "Looped Red Wine", "Plastic Red Wine", "Red Wine Belt", "Corn Red Wine", "Vodka Red Wine", "Red Wine Jar", "Red Wine Holder", "Suede Red Wine", "Purple Red Wine", "Steel Red Wine", "Red Wine Reserve", "Red Wine Weiser", "Red Wine Express", "Express Red Wine", "Quicky Red Wine", "Red Wine Gift", "Dual Red Wine", "Mono Red Wine", "Written Red Wine", "Bag of Red Wine", "Red Wine Con", "Red Wine Shop", "BRB Red Wine", "Hair Red Wine", "Stressed Red Wine", "Timeless Red Wine", "Aged Red Wine", "Poison Red Wine", "Red Wine of the Gods", "Red Wine Empire", "Blast of Red Wine", "Original Red Wine", "Fast Red Wine", "Mega Red Wine", "Red Wine Giant", "Red Wine Patch", "Red Wine 100", "Red Wine Potion", "Red Wine Elixer", "Blue Red Wine", "Red Wine Onion", "Red Wine Bench", "Red Wine Choice", "The Choice of Red Wine", "Red Wine Favorite", "Recess Red Wine", "Red Wine Sport", "Red Wine Armor", "Red Wine Re-fill", "Smiley Red Wine", "Becoming Red Wine", "Wrapped Red Wine", "Red Wine Hair", "Red Wine Soul", "Red Wine Pizza", "Bacon Red Wine", "Red Wine Lips", "Fantastical Red Wine", "Magical Red Wine", "Motivational Red Wine", "Awake Red Wine", "Red Wine Awake", "Red Wine Ready", "Red Wine Alert", "Red Wine Code Red", "Code Red Red Wine", "Mountain Time Red Wine", "Clean Red Wine", "Red Wine Ritual", "Cleansing Red Wine", "Ready Red Win"]
        return names[random.randint(0, len(names)-1)]
        
    def description(self, product):
        template = f"{product} is an alcoholic beverage made from fermented grapes. It is commonly consumed as a drink, but can also be used in cooking. {product} is usually red in color, but it can also be made from other fruits, such as white {product} made from white grapes. {product} is also a key ingredient in several popular drinks, such as sangria and mulled {product}. Red {product} is {product} that is made from red grapes. Red {product} can be drunk on its own, but it is also used in cooking and mixed with other ingredients to make drinks. Red {product} is usually rich in color and has a strong, fruity flavor. Red {product} is also the key ingredient in sangria and mulled {product}."

        return template
        
    def ean(self):
        return str(random.randint(1000000000000, 9999999999999))

    def upc(self):
        return str(random.randint(100000000000, 999999999999))

    def image(self):
        return "http://placeimg.com/640/480/tech"

    def price(self):
        return str(round(random.uniform(1, 99999), 2))

    def netPrice(self):
        return str(round(random.uniform(1, 99999), 2))
        
    def taxes(self):
        return str(random.randint(0, 10))
        
    def category(self, count=3):
        cat = ["Convenience goods", "Shopping goods", "Specialty goods", "Unsought goods"]
        return cat[random.randint(0, len(cat)-1)]