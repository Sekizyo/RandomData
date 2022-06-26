from django.http import HttpResponse, JsonResponse
from engine.addressGen import addressGenerator
from engine.bookGen import bookGenerator
from engine.carGen import carGenerator
from engine.creditCardGen import creditCardGenerator
from engine.dateTimeGen import dateTimeGenerator
from engine.personGen import personGenerator
from engine.placeGen import placeGenerator
from engine.productGen import productGenerator
from engine.textGen import textGenerator
from engine.userGen import userGenerator

addressGen = addressGenerator()
bookGen = bookGenerator()
carGen = carGenerator()
creditCardGen = creditCardGenerator()
dateTimeGen = dateTimeGenerator()
personGen = personGenerator()
placeGen = placeGenerator()
productGen = productGenerator()
textGen = textGenerator()
userGen = userGenerator()

def getResponse(response):
    return JsonResponse(data=response, status=200, safe=False)

def index(request):
    return HttpResponse("Please use one of endpoints like:\n /addresses")

def addresses(request):
    return getResponse(addressGen.getAddress())

def books(request):
    return getResponse(bookGen.getBook())

def cars(request):
    return getResponse(carGen.getCar())

def creditCards(request):
    return getResponse(creditCardGen.getCreditCard())

def dateTime(request, arg):
    return getResponse(dateTimeGen.get(arg))

def persons(request):
    return getResponse(personGen.getPerson())

def places(request):
    return getResponse(placeGen.getPlace())

def products(request):
    return getResponse(productGen.getProduct())

def texts(request):
    return getResponse(textGen.getText())

def users(request):
    return getResponse(userGen.getUser())