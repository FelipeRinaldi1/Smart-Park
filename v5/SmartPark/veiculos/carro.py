from .veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self,placa:str,tipo:str,marca:str,ano:int):
        self.__placa = placa
        self.__tipo = tipo
        self.__marca = marca
        self.__ano = ano

    def get_placa(self):
        return self.__placa

    def get_tipo(self): 
        return self.__tipo
