from concessionaria import Concessionaria
from veiculos.carro import Carro
from veiculos.moto import Moto

veiculo1 = Carro('bmw', 'm3', '2005', '4', '6')
veiculo2 = Concessionaria('mercedes', 'g63', '2010')
veiculo3 = Concessionaria('audi', 'r8', '2013')
veiculo3.alterar_estado()

novaMoto = Moto('bmw', 'g3', '2021', 'Esportiva')

def main():
    Concessionaria.lista_veiculo()
    print(novaMoto)
        
if __name__ == '__main__':
    main()