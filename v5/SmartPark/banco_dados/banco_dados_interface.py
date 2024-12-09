from abc import ABC, abstractmethod

class Banco_Dados_Interface(ABC):
    @abstractmethod
    def adicionar_registro(self):
        pass

    @abstractmethod
    def get_registros(self):
        pass
