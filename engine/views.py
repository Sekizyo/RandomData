from django.http import HttpResponse

from engine.addressGen import addressGenerator
from engine.bookGen import bookGenerator
from engine.creditCardGen import creditCardGenerator
from engine.dateTimeGen import dateTimeGenerator
from engine.personGen import personGenerator
from engine.placeGen import placeGenerator
from engine.productGen import productGenerator
from engine.textGen import textGenerator
from engine.userGen import userGenerator

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
    return jsonify(addressGen.getAddresses())

def books(request):
    return jsonify(bookGen.getBooks())

def creditCards(request):
    return jsonify(creditCardGen.getCreditCards())

def dateTime(request):
    return jsonify(dateTimeGen.get(request))

def persons(request):
    return jsonify(personGen.getPersons())

def places(request):
    return jsonify(placeGen.getPlaces())

def products(request):
    return jsonify(productGen.getProducts())

def texts(request):
    return jsonify(textGen.getTexts())

def users(request):
    return jsonify(userGen.getUsers())