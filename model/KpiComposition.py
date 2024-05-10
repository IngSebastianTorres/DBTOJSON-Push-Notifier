class KpiComposition:
    hist_EjecEther=int()
    hist_EjecHost=int()
    hist_kpiEstimado=int()
    hist_kpiReal=int()

    def __init__(self, hist_EjecEther,hist_EjecHost, hist_kpiEstimado,hist_kpiReal):
        self.hist_EjecEther = hist_EjecEther
        self.hist_EjecHost=hist_EjecHost
        self.hist_kpiEstimado=hist_kpiEstimado
        self.hist_kpiReal=hist_kpiReal

    def to_dict(self):
        return {"hist_EjecEther":self.hist_EjecEther,
                "hist_EjecHost":self.hist_EjecHost,
                "hist_kpiEstimado":self.hist_kpiEstimado,
                "hist_kpiReal":self.hist_kpiReal}