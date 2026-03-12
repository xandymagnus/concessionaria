from concessionaria import Concessionaria

class Carro (Concessionaria):
    carros = []
    
    def __init__(self, marca, modelo, ano, portas=None, assentos=None):
        super().__init__(marca, modelo, ano)
        
        self._portas = str(portas)
        self._assentos = str(assentos)
        self._automatico = False
        Carro.carros.append(self)
        
    def __str__(self):
        return super().__str__() + f' | Portas: {self._portas} | Assentos: {self._assentos} | Automatico: {self._automatico}'
    
    @classmethod
    def lista_carros(cls):
        print(f'{'Marca'.ljust(25)} | {'Modelo'.ljust(25)} | {'Ano'.ljust(25)} | {'Portas'.ljust(25)} | {'Assentos'.ljust(25)} | {'Venda'}\n {'-' * 150}')
        
        for carro in cls.carros:
            if carro._venda == True:
                print(f'{carro._marca.ljust(25)} | {carro._modelo.ljust(25)} | {carro._ano.ljust(25)} | {carro._portas.ljust(25)} | {carro._assentos.ljust(25)} | {carro._venda}')
                