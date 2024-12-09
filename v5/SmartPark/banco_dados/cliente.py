from veiculos import Veiculo, Carro, Moto
class Cliente:
    def __init__(self,cpf:str,nome:str,pcd:bool,cadastro:bool,veiculo:Veiculo):
        self.__cpf = cpf
        self.__nome = nome
        self.__deficiencia = pcd
        self.__cadastro = cadastro
        self.__veiculo = veiculo
        self.__minuto_Entrada = 0
        self.__minuto_Saida = 0

    def get_cpf(self):
        return self.__cpf
    
    def get_nome(self):
        return self.__nome
    
    def get_pcd(self):
        return self.__deficiencia
    
    def get_cadastro(self):
        return self.__cadastro
    
    def get_veiculo(self):
        return self.__veiculo
    
    def get_minuto_Entrada(self):
        return self.__minuto_Entrada
    
    def get_minuto_Saida(self):
        return self.__minuto_Saida
    
    def set_minuto_Entrada(self,minuto_Entrada):
        self.__minuto_Entrada = minuto_Entrada

    def set_minuto_Saida(self,minuto_Saida):
        self.__minuto_Saida = minuto_Saida
    