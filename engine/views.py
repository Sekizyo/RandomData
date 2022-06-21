from django.http import HttpResponse, JsonResponse
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
    return JsonResponse(s.serialize(addressGen.getAddresses()))

def books(request):
    return JsonResponse(s.serialize(bookGen.getBooks()))

def creditCards(request):
    return JsonResponse(s.serialize(creditCardGen.getCreditCards()))

def dateTime(request, arg):
    return JsonResponse(s.serialize(dateTimeGen.get(arg)))

def persons(request):
    return JsonResponse(s.serialize(personGen.getPersons()))

def places(request):
    return JsonResponse(s.serialize(placeGen.getPlaces()))

def products(request):
    return JsonResponse(s.serialize(productGen.getProducts()))

def texts(request):
    return JsonResponse(s.serialize(textGen.getTexts()))

def users(request):
    return JsonResponse(s.serialize(userGen.getUsers()))