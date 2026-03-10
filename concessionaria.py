class Concessionaria():
    veiculos = []
    
    def __init__(self, marca, modelo, ano):
        
        self._marca = marca.upper()
        self._modelo = modelo.upper()
        self._ano = ano
        self._venda = True
        Concessionaria.veiculos.append(self)

    def __str__(self):
        return f'Marca: {self._marca}| Modelo: {self._modelo}| Ano: {self._ano}'
    
    @classmethod
    def lista_veiculo(cls):
        print(f'{'Marca'.ljust(25)} | {'Modelo'.ljust(25)} | {'Ano'.ljust(25)} | {'Venda'}\n')
        
        for veiculo in cls.veiculos:
            print(f'{veiculo._marca.ljust(25)} | {veiculo._modelo.ljust(25)} | {veiculo._ano.ljust(25)} | {veiculo._venda}')
    
    @property
    def ativo(self):
        return '☒' if self._venda == False else '☑'
    
    def alterar_estado(self):
        self._venda = not self._venda