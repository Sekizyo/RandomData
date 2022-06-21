import json
class Serialize():
    def serialize(self, data):
        output = {
            "status": "OK",
            "code": 200,
            "total": len(data),
            "data": data
        }

        return json.dumps(output)