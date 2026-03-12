from concessionaria import Concessionaria

class Moto(Concessionaria):
    motos = []
    
    def __init__(self, marca, modelo, ano, estilo, cor, bagageiro=None):
        super().__init__(marca, modelo, ano)
        
        self._estilo = str(estilo.upper()) if estilo is not None else None
        self._cor = str(cor.upper()) if cor is not None else None
        self._bagageiro = False if bagageiro == '' else True
        Moto.motos.append(self)
        
    def __str__(self):
        return super().__str__() + f' | Estilo: {self._estilo} | Bagageiro: {self._bagageiro}'
    
    @classmethod
    def lista_motos(cls):
        print(f'{'Marca'.ljust(25)} | {'Modelo'.ljust(25)} | {'Ano'.ljust(25)} | {'Estilo'.ljust(25)} | {'Cor'.ljust(25)} | {'Bagageiro'.ljust(25)} | {'Venda'}\n {'-' * 190}')
        
        for moto in cls.motos:
            if moto._venda == True:
                print(f'{moto._marca.ljust(25)} | {moto._modelo.ljust(25)} | {moto._ano.ljust(25)} | {moto._estilo.ljust(25)} | {moto._cor.ljust(25)} | {'Sim'.ljust(25) if moto._bagageiro == True else 'Nâo'.ljust(25)} | {moto._venda}')