import model.KpiComposition as KpiComposition

class Days:
 
    date = object
    kpi_global = KpiComposition
    kpi_core= KpiComposition
    kpi_online= KpiComposition

    def __init__(self, date, kpi_global,kpi_core, kpi_online):
        self.date=date
        self.kpi_core = kpi_core
        self.kpi_global=kpi_global
        self.kpi_online=kpi_online

    def to_dict(self):
        return {"date":self.date,"kpi_global":self.kpi_global.to_dict(),"kpi_core":self.kpi_core.to_dict(),"kpi_online":self.kpi_online.to_dict()}