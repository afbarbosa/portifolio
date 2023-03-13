class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato (self):
        print("O valor do extrato é {}".format(self.__saldo))
    
    def __pode_sacar(self, valor_sacar):
        valor_total = self.__saldo + self.__limite
        return valor_sacar < valor_total
    
    def saque (self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Seu limite de saque é {}".format((self.__limite + self.__saldo)))
        
    def deposita (self, valor):
        self.__saldo += valor

    def transfere (self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
    @property
    def numero(self):
        return self.__numero
        
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
        
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite 
        
    @staticmethod
    def codigos_bancos ():
        return {"Banco do Brasil": "001", "Caixa Econômica": "104","Bradesco":"237","Nubank":"266"}