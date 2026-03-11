from concessionaria import Concessionaria
from veiculos.carro import Carro
from veiculos.moto import Moto

def atributos_carro():
    print('Adicione os atributos:\n')
     
    marca = input('Marca: ')
    modelo = input('Modelo: ')
    ano = input('Ano: ')
    portas = input('Portas: ')
    assentos = input('Assentos: ')
    
    return marca, modelo, ano, portas, assentos

def atributos_moto():
    pass

veiculo1 = Carro(*atributos_carro())
veiculo2 = Carro(*atributos_carro())
veiculo3 = Carro(*atributos_carro())
novaMoto = Moto('bmw', 'g3', '2021', 'Esportiva')


def main():
    Concessionaria.lista_veiculo()
    print('2' == 2)
if __name__ == '__main__':
    main()