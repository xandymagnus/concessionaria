from concessionaria import Concessionaria
from veiculos.carro import Carro
from veiculos.moto import Moto

def atributos_concessionaria():
    print('\nAdicione os atributos:\n')
    
    marca = input('Marca: ')
    modelo = input('Modelo: ')
    ano = input('Ano: ')
    
    return marca, modelo, ano

def atributos_carro():
    print('\nCriando carro...')
    
    marca, modelo, ano = atributos_concessionaria()

    portas = input('Portas: ')
    assentos = input('Assentos: ')
    automatico = input('Automático: ')
    
    return marca, modelo, ano, portas, assentos, automatico

def atributos_moto():
    print('\nCriando moto...')
    
    marca, modelo, ano = atributos_concessionaria()
    
    estilo = input('Estilo: ')
    cor = input('Cor: ')
    
    return marca, modelo, ano, estilo, cor

# moto1 = Moto(*atributos_moto())
# moto1.alterar_estado()

# moto2 = Moto(*atributos_moto())
# moto3 = Moto(*atributos_moto())
# veiculo2 = Concessionaria('bmw', '312', '2019')

carro1 = Carro(*atributos_carro())

novaMoto = Moto('bmw', 'g3', '2021', 'Esportiva', 'Preta')


def main():
    Carro.lista_carros()
    print('\n')
    Moto.lista_motos()
    print('\n')
    Concessionaria.lista_veiculo()
    
if __name__ == '__main__':
    main()