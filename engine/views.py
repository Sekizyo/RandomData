from django.http import HttpResponse
from engine.serialize import Serialize
from engine.addressGen import addressGenerator
from engine.bookGen import bookGenerator
from engine.creditCardGen import creditCardGenerator
from engine.dateTimeGen import dateTimeGenerator
from engine.personGen import personGenerator
from engine.placeGen import placeGenerator
from engine.productGen import productGenerator
from engine.textGen import textGenerator
from engine.userGen import userGenerator

s = Serialize()

addressGen = addressGenerator()
bookGen = bookGenerator()
creditCardGen = creditCardGenerator()
dateTimeGen = dateTimeGenerator()
personGen = personGenerator()
placeGen = placeGenerator()
productGen = productGenerator()
textGen = textGenerator()
userGen = userGenerator()

def index(request):
    return HttpResponse("Please use one of endpoints like:\n /addresses")

def addresses(request):
    return s.response(addressGen.getAddresses())

def books(request):
    return s.response(bookGen.getBooks())

def creditCards(request):
    return s.response(creditCardGen.getCreditCards())

def dateTime(request, arg):
    return s.response(dateTimeGen.get(arg))

def persons(request):
    return s.response(personGen.getPersons())

def places(request):
    return s.response(placeGen.getPlaces())

def products(request):
    return s.response(productGen.getProducts())

def texts(request):
    return s.response(textGen.getTexts())

def users(request):
    return s.response(userGen.getUsers())