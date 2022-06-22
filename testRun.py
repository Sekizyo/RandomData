from engine.addressGen import addressGenerator
from engine.serialize import Serialize

s = Serialize()

addressGen = addressGenerator()

output = s.serialize(addressGen.getAddresses())
print(type(output))