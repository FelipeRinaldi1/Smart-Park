from  importacao import *
class Controlador():
    def __init__(self,banco_dados: Banco_Dados_Interface,estacionamento:Estacionamento_Interface):
        self.__banco_dados = banco_dados
        self.__estacionamento = estacionamento

    def get_estacionamento(self):
        return self.__estacionamento

    def registrar_veiculo(self, placa: str, tipo_veiculo: str, marca: str, ano: int, cpf: str, nome: str, deficiente: bool, cadastrado: bool, minuto_entrada: int, minuto_saida: int, numero_vaga: int):
        if tipo_veiculo == "Carro":
            veiculo = Carro(placa, tipo_veiculo, marca, ano)
        else:
            veiculo = Moto(placa, tipo_veiculo, marca, ano)
        cliente = Cliente(cpf, nome, deficiente, cadastrado, veiculo)
        cliente.set_minuto_Entrada(minuto_entrada)
        cliente.set_minuto_Saida(minuto_saida)

        comprovante = Comprovante_Estacionamento(cliente)
        
        comprovante.set_Numero_Vaga(numero_vaga)

        self.__estacionamento.selecionar_vaga(numero_vaga)  
        self.__banco_dados.adicionar_registro(comprovante)


    def exibir_registros(self):
        registros = self.__banco_dados.get_registros()
        if registros:
            for registro in registros:
                print(f"\nNome: {registro.get_Nome()} pertencente ao CPF: {registro.get_CPF()}")
                print(f"Detentor do veículo de placa: {registro.get_Placa_Veiculo()}")
                print(f"sendo esse veículo um(a) {registro.get_Tipo_Veiculo()}")
                print(f"Tipo do usuário: {registro.get_Tipo_Usuario()}")
                print(f"Tempo total: {registro.get_Tempo_Total()} minutos")
                print(f"Custo: R$ {registro.get_Custo():.2f}")
                print(f"Horário de entrada: {registro.get_Horario_Entrada()} minutos")
                print(f"Horário de saída: {registro.get_Horario_Saida()} minutos")
                print(f"Vaga Ocupada: {registro.get_Numero_Vaga()}")

    def buscar_registro_por_placa(self, placa: str):
        registros = self.__banco_dados.get_registros()
        for registro in registros:
            if registro.get_Placa_Veiculo() == placa:
                print(f"\nNome: {registro.get_Nome()}")
                print(f"CPF: {registro.get_CPF()}")
                print(f"Placa: {registro.get_Placa_Veiculo()}")
                print(f"Tipo de veículo: {registro.get_Tipo_Veiculo()}")
                print(f"Tipo de usuário: {registro.get_Tipo_Usuario()}")
                print(f"Tempo total de estacionamento: {registro.get_Tempo_Total()} minutos")
                print(f"Custo: R$ {registro.get_Custo():.2f}")
                print(f"Horário de entrada: {registro.get_Horario_Entrada()} minutos")
                print(f"Horário de saída: {registro.get_Horario_Saida()} minutos")
                return
        print("Registro não encontrado.")
    
    def apagar_registro_por_placa(self, placa: str):
        registros = self.__banco_dados.get_registros()
        for registro in registros:
            if registro.get_Placa_Veiculo() == placa:
                numero_vaga = registro.get_Numero_Vaga()  
                self.__estacionamento.liberar_vaga(numero_vaga)
                self.__banco_dados.get_registros().remove(registro)
                print(f"Registro do veículo com placa {placa} apagado e vaga {numero_vaga} desocupada com sucesso.")
                return
        print("Registro não encontrado para apagar.")


    def exibir_vagas(self):
        vagas = self.__estacionamento.get_vagas()
        print("Mapa de Vagas:")
        for i, vaga in enumerate(vagas):
            if i % 5 == 0 and i != 0:
                print()
            if vaga.e_Ocupada():
                print("X ", end="")
            else:
                print(f"{i + 1} ", end="")
        print()