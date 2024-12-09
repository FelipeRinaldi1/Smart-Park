from estacionamento.estacionamento import Estacionamento
from controlador import Controlador
class InputOutput:
    def __init__(self, controlador:Controlador):
        self.controlador = controlador

    def executar(self):
        # Validação placa
        placa = ""
        while len(placa) != 7:
            placa = input("Digite a placa do veículo (7 caracteres): ")
            if len(placa) != 7:
                print("Placa inválida. Certifique-se de que tem exatamente 7 caracteres.")

        # Validação veículo
        tipo_veiculo = ""
        while tipo_veiculo not in ["Carro", "Moto"]:
            tipo_veiculo = input("Digite o tipo do veículo (Carro ou Moto): ")
            if tipo_veiculo not in ["Carro", "Moto"]:
                print("Tipo de veículo inválido. Escolha 'Carro' ou 'Moto'.")

        # Validação marca
        marca = ""
        while len(marca) > 20 or len(marca) == 0:
            marca = input("Digite a marca do veículo (até 20 caracteres): ")
            if len(marca) > 20:
                print("Marca inválida. Certifique-se de que tenha no máximo 20 caracteres.")
            elif len(marca) == 0:
                print("Marca inválida. Não pode estar vazia.")

        # Validação ano
        ano_valido = False
        while not ano_valido:
            ano = input("Digite o ano do veículo (entre 1900 e 2024): ")
            if ano.isdigit():
                ano = int(ano)
                if 1900 <= ano <= 2024:
                    ano_valido = True
                else:
                    print("Ano inválido. Certifique-se de que esteja entre 1900 e 2024.")
            else:
                print("Ano inválido. Digite um número.")

        # Validação CPF
        cpf = ""
        while len(cpf) != 11 or not cpf.isdigit():
            cpf = input("Digite o CPF do cliente (11 dígitos): ")
            if len(cpf) != 11 or not cpf.isdigit():
                print("CPF inválido. Certifique-se de que tenha exatamente 11 dígitos.")

        # Validação nome
        nome = ""
        while len(nome) > 50 or len(nome) == 0:
            nome = input("Digite o nome do cliente (até 50 caracteres): ")
            if len(nome) > 50:
                print("Nome inválido. Certifique-se de que tenha no máximo 50 caracteres.")
            elif len(nome) == 0:
                print("Nome inválido. Não pode estar vazio.")

        # Validação pcd
        deficiente = None
        while deficiente not in [1, 2]:
            deficiente_input = input("O cliente é deficiente? (1 para Sim, 2 para Não): ")
            if deficiente_input.isdigit():
                deficiente = int(deficiente_input)
                if deficiente not in [1, 2]:
                    print("Opção inválida. Escolha 1 (Sim) ou 2 (Não).")
            else:
                print("Opção inválida. Digite 1 ou 2.")
        deficiente = deficiente == 1

        # Validação cadastro
        cadastrado = None
        while cadastrado not in [1, 2]:
            cadastrado_input = input("O cliente é cadastrado? (1 para Sim, 2 para Não): ")
            if cadastrado_input.isdigit():
                cadastrado = int(cadastrado_input)
                if cadastrado not in [1, 2]:
                    print("Opção inválida. Escolha 1 (Sim) ou 2 (Não).")
            else:
                print("Opção inválida. Digite 1 ou 2.")
        cadastrado = cadastrado == 1

        # Validação entrada
        minuto_entrada = -1
        while minuto_entrada < 0 or minuto_entrada > 1440:
            entrada_input = input("Digite o horário de entrada (em minutos, 0 a 1440): ")
            if entrada_input.isdigit():
                minuto_entrada = int(entrada_input)
                if minuto_entrada < 0 or minuto_entrada > 1440:
                    print("Horário de entrada inválido. Certifique-se de que esteja entre 0 e 1440 minutos.")
            else:
                print("Horário de entrada inválido. Digite um número.")

        # Validação saída
        minuto_saida = -1
        while minuto_saida <= minuto_entrada or minuto_saida > 1440:
            saida_input = input("Digite o horário de saída (em minutos, 0 a 1440): ")
            if saida_input.isdigit():
                minuto_saida = int(saida_input)
                if minuto_saida <= minuto_entrada or minuto_saida > 1440:
                    print("Horário de saída inválido. Deve ser maior que o horário de entrada e estar entre 0 e 1440 minutos.")
            else:
                print("Horário de saída inválido. Digite um número.")

        self.controlador.exibir_vagas()

        # Validação  vaga
        numero_vaga = -1
        while numero_vaga < 1 or numero_vaga > len(self.controlador.get_estacionamento().get_vagas()):
            vaga_input = input(f"Escolha uma vaga (1 a {len(self.controlador.get_estacionamento().get_vagas())}): ")
            if vaga_input.isdigit():
                numero_vaga = int(vaga_input)
                if numero_vaga < 1 or numero_vaga > 20:
                    print(f"Vaga inválida. Escolha um número entre 1 e {len(self.controlador.get_estacionamento().get_vagas())}.")
            else:
                print(f"Vaga inválida. Digite um número entre 1 e {len(self.controlador.get_estacionamento().get_vagas())}.")

        self.controlador.registrar_veiculo(
            placa, tipo_veiculo, marca, ano, cpf, nome,
            deficiente, cadastrado, minuto_entrada, minuto_saida, numero_vaga)

        print("Registro efetuado com sucesso.")