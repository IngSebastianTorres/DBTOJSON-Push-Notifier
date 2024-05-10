import model.Months as Months
class Years:
    year = int()
    kpi_annual = Months

    def __init__(self,year,kpi_annual):
        self.year=year
        self.kpi_annual=kpi_annual

    def to_dict(self):
       return {"year": self.year,"kpi_annual":self.kpi_annual.to_dict()}
