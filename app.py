from concessionaria import Concessionaria
from veiculos.carro import Carro


veiculo1 = Concessionaria('bmw', 'm3', '2005')
veiculo2 = Concessionaria('mercedes', 'g63', '2010')
veiculo3 = Concessionaria('audi', 'r8', '2013')
veiculo3.alterar_estado()

def main():
    Concessionaria.lista_veiculo()
        
if __name__ == '__main__':
    main()