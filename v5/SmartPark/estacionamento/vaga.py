class Vaga():
    def __init__(self):
        self.__ocupada = False
    
    def e_Ocupada(self):
        return self.__ocupada
    
    def ocupar(self):
        self.__ocupada = True

    def liberar(self):
        self.__ocupada = False