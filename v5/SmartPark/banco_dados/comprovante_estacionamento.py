from .cliente import Cliente

class Comprovante_Estacionamento:
    def __init__(self,cliente:Cliente):     
        self.__cliente = cliente
        minutos = cliente.get_minuto_Saida() - cliente.get_minuto_Entrada()
        self.__custo = self.__calcular_custo(minutos)
        self.__numero_vaga = None  

    def __calcular_custo(self,minutos):
        tarifa_30min = 3
        custo_Base = (minutos/30)*tarifa_30min
        if (self.__cliente.get_cadastro()):
            custo_Base = custo_Base*0.9
        if (self.__cliente.get_pcd()):
            custo_Base = custo_Base*0.8
        return custo_Base

    def get_Placa_Veiculo(self):
        return self.__cliente.get_veiculo().get_placa()
    
    def get_Tipo_Veiculo(self):
        return self.__cliente.get_veiculo().get_tipo()
    
    def get_Tipo_Usuario(self):
        if (self.__cliente.get_cadastro()):
            return "Cadastrado"
        else:
            return "Nao Cadastrado"
        
    def get_Nome(self):
        return self.__cliente.get_nome()
    
    def get_CPF(self):
        return self.__cliente.get_cpf()
    
    def get_Custo(self):
        return self.__custo
    
    def get_Tempo_Total(self):
        return self.__cliente.get_minuto_Saida() - self.__cliente.get_minuto_Entrada()
    
    def get_Horario_Entrada(self):
        return self.__cliente.get_minuto_Entrada()
    
    def get_Horario_Saida(self):
        return self.__cliente.get_minuto_Saida()

    def set_Numero_Vaga(self, numero_vaga):
        self.__numero_vaga = numero_vaga

    def get_Numero_Vaga(self):
        return self.__numero_vaga