from engine.addressGen import addressGenerator
from engine.serialize import Serialize
from django.http import JsonResponse
import json
s = Serialize()

addressGen = addressGenerator()

# output = JsonResponse(data=addressGen.getAddresses(), status=200, safe=False)
# print(output)
output = [
    "{\"streetname\": \"Austin Garth\", \"country\": \"Brazil\", \"countryCode\": \"1-409\", \"city\": \"Tokyo\", \"zipcode\": \"03695\", \"buildingnumber\": \"999\", \"latitude\": \"-12.8253569\", \"longitude\": \"1.6922726\"}",
    "{\"streetname\": \"Allen Wharf\", \"country\": \"Italy\", \"countryCode\": \"1-353\", \"city\": \"Dhaka\", \"zipcode\": \"22585\", \"buildingnumber\": \"793\", \"latitude\": \"3.1634266\", \"longitude\": \"-67.3183299\"}",
    "{\"streetname\": \"Artington Close\", \"country\": \"Lithuenia\", \"countryCode\": \"1-180\", \"city\": \"Cairo\", \"zipcode\": \"59912\", \"buildingnumber\": \"91\", \"latitude\": \"-71.6541682\", \"longitude\": \"46.5137736\"}",
    "{\"streetname\": \"Austin Garth\", \"country\": \"Australia\", \"countryCode\": \"1-101\", \"city\": \"Mexico City\", \"zipcode\": \"2545\", \"buildingnumber\": \"691\", \"latitude\": \"55.6602008\", \"longitude\": \"-24.2417634\"}",
    "{\"streetname\": \"Austin Garth\", \"country\": \"India\", \"countryCode\": \"1-418\", \"city\": \"Paris\", \"zipcode\": \"56992\", \"buildingnumber\": \"12\", \"latitude\": \"-84.1490743\", \"longitude\": \"65.9608019\"}",
    "{\"streetname\": \"Armstrong Parkway\", \"country\": \"Austria\", \"countryCode\": \"1-351\", \"city\": \"Paris\", \"zipcode\": \"94051\", \"buildingnumber\": \"913\", \"latitude\": \"21.9969967\", \"longitude\": \"62.5196522\"}",
    "{\"streetname\": \" Alissa Drive\", \"country\": \"France\", \"countryCode\": \"1-437\", \"city\": \"Madrit\", \"zipcode\": \"36287\", \"buildingnumber\": \"880\", \"latitude\": \"45.7563891\", \"longitude\": \"37.1484373\"}",
    "{\"streetname\": \" Alissa Drive\", \"country\": \"Brazil\", \"countryCode\": \"1-435\", \"city\": \"Beijing\", \"zipcode\": \"45389\", \"buildingnumber\": \"715\", \"latitude\": \"36.7511386\", \"longitude\": \"76.8149116\"}",
    "{\"streetname\": \"Allen Wharf\", \"country\": \"Italy\", \"countryCode\": \"1-455\", \"city\": \"Mumbai\", \"zipcode\": \"31253\", \"buildingnumber\": \"573\", \"latitude\": \"66.7490029\", \"longitude\": \"64.6877526\"}",
    "{\"streetname\": \"Austin Garth\", \"country\": \"Lithuenia\", \"countryCode\": \"1-247\", \"city\": \"Sao Paulo\", \"zipcode\": \"7894\", \"buildingnumber\": \"233\", \"latitude\": \"13.1160898\", \"longitude\": \"-61.843894\"}"
]
y = json.loads(output)
print(y)