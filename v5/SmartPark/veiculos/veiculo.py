from abc import ABC,abstractmethod

class Veiculo(ABC):
    def __init__(self,placa:str,tipo:str,marca:str,ano:int):
        self.__placa = placa
        self.__tipo = tipo
        self.__marca = marca
        self.__ano = ano

    @abstractmethod
    def get_placa(self):
        pass
    @abstractmethod
    def get_tipo(self): 
        pass
