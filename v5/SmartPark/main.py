from importacao import * 
from controlador import *
from InputOutput import *
def main():

    banco_dados = Banco_Dados()
    estacionamento = Estacionamento(50)
    controlador = Controlador(banco_dados, estacionamento)
    interface = InputOutput(controlador)
    print("\nGerenciamento de Estacionamento - SmartPark")
    while True:

        print("\nEscolha uma opção:")
        print("1) Registrar Veículo")
        print("2) Remover Veículo")
        print("3) Exibir Registros")
        print("4) Exibir Mapa de Vagas")
        print("5) Buscar Registro por Placa")
        print("0) Sair")
        opcao = input("Escolha uma opção: \n")

        if opcao == "1":
            interface.executar()
        elif opcao == "2":
            placa_remocao = input("Digite a placa do veículo para remoção: ")
            controlador.apagar_registro_por_placa(placa_remocao)
        elif opcao == "3":
            controlador.exibir_registros()
        elif opcao == "4":
            controlador.exibir_vagas()
        elif opcao == "5":
            placa_busca = input("Digite a placa do veículo para buscar: ")
            controlador.buscar_registro_por_placa(placa_busca)
        elif opcao == "0":
            print("Encerrando o SmartPark.\n")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()  