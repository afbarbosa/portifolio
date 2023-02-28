class Conta:
    def __init__(self, numero, titular, saldo, limite):
        Conta.numero = numero
        Conta.titular = titular
        Conta.saldo = saldo
        Conta.limite = limite
        
    def extrato (self):
        print("O valor do extrato é {}".format(self.saldo))
    
    def saque (self, valor):
        self.saldo -= valor
        
    def deposita (self, valor):
        self.saldo += valor          