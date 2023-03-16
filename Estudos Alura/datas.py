class Data:
    def __init__(self,dia,mes,ano):
        Data.dia = dia
        Data.mes = mes
        Data.ano = ano
    
    def formatada(self):
        print("{}/{}/{}".format(self.dia,self.mes,self.ano))