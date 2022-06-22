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

def getResponse(response):
    return s.response(response)

def index(request):
    return HttpResponse("Please use one of endpoints like:\n /addresses")

def addresses(request):
    return getResponse(addressGen.getAddresses())

def books(request):
    return getResponse(bookGen.getBooks())

def creditCards(request):
    return getResponse(creditCardGen.getCreditCards())

def dateTime(request, arg):
    return getResponse(dateTimeGen.get(arg))

def persons(request):
    return getResponse(personGen.getPersons())

def places(request):
    return getResponse(placeGen.getPlaces())

def products(request):
    return getResponse(productGen.getProducts())

def texts(request):
    return getResponse(textGen.getTexts())

def users(request):
    return getResponse(userGen.getUsers())