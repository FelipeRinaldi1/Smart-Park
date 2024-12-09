from .estacionamento_interface import Estacionamento_Interface
from .vaga import Vaga
class Estacionamento(Estacionamento_Interface):
    def __init__(self,vagas):
        self.__vagas = []
        for i in range(vagas):
            self.__vagas.append(Vaga())

    def selecionar_vaga(self,numero_Vaga:int):
        if self.__vagas[numero_Vaga-1].e_Ocupada():
            print("A vaga já está ocupada.\n")
        else:
            self.__vagas[numero_Vaga-1].ocupar()
            print("Vaga ocupada com sucesso.\n")

    def liberar_vaga(self,numero_Vaga:int):
        if self.__vagas[numero_Vaga-1].e_Ocupada():
           self.__vagas[numero_Vaga-1].liberar() 

    def get_vagas(self):
        return self.__vagas

