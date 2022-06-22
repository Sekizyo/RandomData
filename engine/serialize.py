import json
from django.http import JsonResponse
class Serialize():
    def response(self, data):
        output = {
            "status": "OK",
            "code": 200,
            "total": len(data),
            "data": data
        }

        return JsonResponse(json.dumps(output))