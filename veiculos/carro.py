from concessionaria import Concessionaria

class Carro (Concessionaria):
    def __init__(self, marca, modelo, ano, portas, assentos):
        super().__init__(marca, modelo, ano)
        
        self._portas = portas
        self._assentos = assentos
        
    def __str__(self):
        return super().__str__() + f' | Portas: {self._portas} | Assentos: {self._assentos}'
         