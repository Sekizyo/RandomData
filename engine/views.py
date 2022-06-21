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

serialize = Serialize()

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
    return JsonResponse(serialize(addressGen.getAddresses()))

def books(request):
    return JsonResponse(serialize(bookGen.getBooks()))

def creditCards(request):
    return JsonResponse(serialize(creditCardGen.getCreditCards()))

def dateTime(request, arg):
    return JsonResponse(serialize(dateTimeGen.get(arg)))

def persons(request):
    return JsonResponse(serialize(personGen.getPersons()))

def places(request):
    return JsonResponse(serialize(placeGen.getPlaces()))

def products(request):
    return JsonResponse(serialize(productGen.getProducts()))

def texts(request):
    return JsonResponse(serialize(textGen.getTexts()))

def users(request):
    return JsonResponse(serialize(userGen.getUsers()))