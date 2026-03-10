from concessionaria import Concessionaria

class Moto(Concessionaria):
    def __init__(self, marca, modelo, ano, estilo):
        super().__init__(marca, modelo, ano)
        
        self._estilo = estilo
        self._bagageiro = False
        
        