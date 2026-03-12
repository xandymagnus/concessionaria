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
    print('\n')
    
    return marca, modelo, ano, portas, assentos

def atributos_moto():
    pass

veiculo1 = Carro(*atributos_carro())
veiculo1.alterar_estado()
carro1 = Carro(*atributos_carro())
carro2 = Carro(*atributos_carro())
veiculo2 = Concessionaria('bmw', '312', '2019')

novaMoto = Moto('bmw', 'g3', '2021', 'Esportiva')


def main():
    Carro.lista_carros()
    Carro.lista_veiculo()
    
if __name__ == '__main__':
    main()