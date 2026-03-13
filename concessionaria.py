class Concessionaria():
    """
    Responsável por administrar uma concessionária que adiciona, deleta e muda estados dos veículos
    """
    
    veiculos = []
    
    def __init__(self, marca, modelo, ano):
        
        """
        Inicializa a concessionaria:
        
        :param marca: str - Marca do veículo.
        :param modelo: str - Modelo do veículo.
        :param ano: str - Ano do veículo.
        :param venda: bool - Se o veículo está disponível para venda.
        """
        
        self._marca = str(marca.upper())
        self._modelo = str(modelo.upper())
        self._ano = str(ano)
        self._venda = True
        Concessionaria.veiculos.append(self)

    def __str__(self):
        return f'Marca: {self._marca}| Modelo: {self._modelo}| Ano: {self._ano}'
    
    @classmethod
    def lista_veiculo(cls):
        print(f'{'Marca'.ljust(25)} | {'Modelo'.ljust(25)} | {'Ano'.ljust(25)} | {'Venda'}\n {'-' * 90}')
        
        for veiculo in cls.veiculos:
            if veiculo._venda == True:
                print(f'{veiculo._marca.ljust(25)} | {veiculo._modelo.ljust(25)} | {veiculo._ano.ljust(25)} | {veiculo._venda}')
    
    @property
    def ativo(self):    
        return '☒' if self._venda == False else '☑'
    
    def alterar_estado(self):
        """
        Modifica estado do atributo venda invertendo seu valor booleano.
        
        Args:
            self - Instancia do objeto
        """
        
        self._venda = not self._venda