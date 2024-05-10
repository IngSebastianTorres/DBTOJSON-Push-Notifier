import model.Days as Days

class Months:
   
    enero=[Days]
    febrero=[Days]
    marzo=[Days]
    abril=[Days]
    mayo=[Days]
    junio=[Days]
    julio=[Days]
    agosto=[Days]
    septiembre=[Days]
    octubre=[Days]
    noviembre=[Days]
    diciembre=[Days]

    def __init__(self, enero=[Days],febrero=[Days],marzo=[Days],abril=[Days],mayo=[Days],junio=[Days],julio=[Days],agosto=[Days]
                 ,septiembre=[Days],octubre=[Days],noviembre=[Days],diciembre=[Days]):
        self.enero = enero
        self.febrero = febrero
        self.marzo = marzo
        self.abril = abril
        self.mayo = mayo
        self.junio = junio
        self.julio = julio
        self.agosto = agosto
        self.septiembre = septiembre
        self.octubre = octubre
        self.noviembre= noviembre
        self.diciembre = diciembre

    def to_dict(self):
        return {
                "enero":[day.to_dict() for day in self.enero],
                "febrero":[day.to_dict() for day in self.febrero],
                "marzo":[day.to_dict() for day in self.marzo],
                "abril":[day.to_dict() for day in self.abril],
                "mayo":[day.to_dict() for day in self.mayo],
                "junio":[day.to_dict() for day in self.junio],
                "julio":[day.to_dict() for day in self.julio],
                "agosto":[day.to_dict() for day in self.agosto], 
                "septiembre":[day.to_dict() for day in self.septiembre], 
                "octubre":[day.to_dict() for day in self.octubre],
                "noviembre":[day.to_dict() for day in self.noviembre],
                "diciembre":[day.to_dict() for day in self.diciembre]
        }