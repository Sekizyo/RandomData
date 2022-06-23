import random

def firstName():
        firstNames = ["Maria", "Nushi", "Mohammed", "Jose", "Wei", "Yan", "David", "John", "Ana", "Michael"]
        return firstNames[random.randint(0, len(firstNames)-1)]

def lastName():
    lastNames = ["Wang", "Smith", "Devi", "Ivanov", "Kim", "Ali", "Garcia", "Silva", "Hansen"]
    return lastNames[random.randint(0, len(lastNames)-1)]