import model.Years as Years
class Data:
        
    data = [Years]

    def __init__(self, data = [Years]):
        self.data=data

    def to_dict(self):
        return {"data": [year.to_dict() for year in self.data]}