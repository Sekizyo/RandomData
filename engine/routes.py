from engine import app
from flask import request, jsonify
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

@app.route('/', methods=['GET'])
def home():
    return "Please use one of endpoints like:\n /addresses"

@app.route('/addresses', methods=['GET'])
def addresses():
    return jsonify(addressGen.getAddresses())

@app.route('/books', methods=['GET'])
def books():
    return jsonify(bookGen.getBooks())

@app.route('/credit_cards', methods=['GET'])
def creditCards():
    return jsonify(creditCardGen.getCreditCards())

@app.route('/date_time/<arg>', methods=['GET'])
def dateTime(arg):
    return jsonify(dateTimeGen.get(arg))

@app.route('/persons', methods=['GET'])
def persons():
    return jsonify(personGen.getPersons())

@app.route('/places', methods=['GET'])
def places():
    return jsonify(placeGen.getPlaces())

@app.route('/products', methods=['GET'])
def products():
    return jsonify(productGen.getProducts())

@app.route('/texts', methods=['GET'])
def texts():
    return jsonify(textGen.getTexts())

@app.route('/users', methods=['GET'])
def users():
    return jsonify(userGen.getUsers())