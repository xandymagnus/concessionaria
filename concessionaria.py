class Concessionaria():
    def __init__(self, marca, modelo, ano):
        veiculos = []
        
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._venda = True

    def __str__(self):
        return f'Marca: {self._marca}| Modelo: {self._modelo}| Ano: {self._ano}'
    
          
        
        