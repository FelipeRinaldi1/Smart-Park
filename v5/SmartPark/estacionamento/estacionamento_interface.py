from abc import ABC, abstractmethod

class Estacionamento_Interface(ABC):
    @abstractmethod
    def selecionar_vaga(self, numero_vaga: int):
        pass

    @abstractmethod
    def get_vagas(self):
        pass

    @abstractmethod
    def liberar_vaga(self):
        pass