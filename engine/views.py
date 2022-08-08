from django.http import HttpResponse, JsonResponse
from engine.addressGen import addressGenerator
from engine.bookGen import bookGenerator
from engine.carGen import carGenerator
# from engine.containerGen import containerGenerator
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
# containerGen = containerGenerator()
creditCardGen = creditCardGenerator()
dateTimeGen = dateTimeGenerator()
personGen = personGenerator()
placeGen = placeGenerator()
productGen = productGenerator()
textGen = textGenerator()
userGen = userGenerator()

def getJsonResponse(response):
    return JsonResponse(data=response, status=200, safe=True)

def getResponse(response):
    return JsonResponse(data=response, status=200, safe=False)

def index(request):
    return HttpResponse("Please use one of endpoints like:\n /addresses")

def address(request):
    return getJsonResponse(addressGen.getAddress())

def book(request):
    return getJsonResponse(bookGen.getBook())

def car(request):
    return getJsonResponse(carGen.getCar())

# def container(request):
#     return getJsonResponse(containerGen.getContainer())

def creditCard(request):
    return getJsonResponse(creditCardGen.getCreditCard())

def cctransactions(request):
    return getResponse(creditCardGen.getCCTransactions())

def dateTime(request, arg):
    return getJsonResponse(dateTimeGen.get(arg))

def person(request):
    return getJsonResponse(personGen.getPerson())

def place(request):
    return getJsonResponse(placeGen.getPlace())

def product(request):
    return getJsonResponse(productGen.getProduct())

def text(request):
    return getJsonResponse(textGen.getText())

def user(request):
    return getJsonResponse(userGen.getUser())