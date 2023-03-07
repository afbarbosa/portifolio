class Conta:
    def __init__(self, numero, titular, saldo, limite):
        Conta.__numero = numero
        Conta.__titular = titular
        Conta.__saldo = saldo
        Conta.__limite = limite
        
    def extrato (self):
        print("O valor do extrato é {}".format(self.__saldo))
    
    def saque (self, valor):
        self.__saldo -= valor
        
    def deposita (self, valor):
        self.__saldo += valor

    def tranfere (self, valor, origem, destino):
        origem.saca(valor)
        destino.deposita(valor)