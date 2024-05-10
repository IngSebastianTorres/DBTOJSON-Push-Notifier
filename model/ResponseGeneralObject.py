import model.Years as Years
import model.Data as Data
import json

class ResponseGeneralObject:

    status=200
    message = ""
    response=Data

    def __init__(self,status,message,response):
        self.response=response
        self.status=status
        self.message=message


    def toJSON(self):
        return json.dumps({
            "status": self.status,
            "message": self.message,
            "response": self.response.to_dict()
        }, sort_keys=True, indent=2)