from .comprovante_estacionamento import Comprovante_Estacionamento
from .banco_dados_interface import Banco_Dados_Interface
class Banco_Dados(Banco_Dados_Interface):
    def __init__(self):
        self.__registros = []

    def adicionar_registro(self,registro:Comprovante_Estacionamento):
        self.__registros.append(registro)

    def get_registros(self):
        return self.__registros
