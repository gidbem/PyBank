class Conta:
    def __init__(self, numero, titular, saldo):
        #Encapsulando os atributos
        #_ protegido (protected) (apenas as classes filhas tem acesso)
        #__ privado (private) (apenas a própria classe tem acesso)
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

    #GET --> captura a variável (sempre com retorno)
    def get_saldo(self):
        return self.__saldo

    #SET --> altera uma variável (sempre sem retorno)
    def saque(self, valor):
        if self.__saldo - valor <= 0 or valor < 0:
            print('Saldo insuficiente ou valor inválido')
        else:
            self.__saldo -= valor
            return True

    def deposito(self, valor):
        if valor <= 0:
            print('Valor inválido para depósito')
        else:
            self.__saldo += valor
            return False

#__________________________________________________________________ aula dia 16/03 (continuação)
    '''
    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular
    '''
    #Equivalente ao GET
    @property #decorator
    def titular(self):
        return self.__titular

    #Equivalete ao SET
    @titular.setter
    def titular(self, titular):
        if len(titular) > 1:
            self.__titular = titular
        else:
            print('O nome deve ter mais de 1 caractere')
    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero


    def transfere(self, valor, favorecido):
        if self.saque(valor):
            favorecido.deposito(valor)

