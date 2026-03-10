from concessionaria import Concessionaria

class Moto(Concessionaria):
    def __init__(self, marca, modelo, ano, estilo):
        super().__init__(marca, modelo, ano)
        
        self._estilo = estilo
        self._bagageiro = False
        
    def __str__(self):
        return super().__str__() + f' | Estilo: {self._estilo} | Bagageiro: {self._bagageiro}'