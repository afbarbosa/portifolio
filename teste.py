def cria_conta(numero, titular, saldo, limite):
    conta = {"numero":numero, "titular": titular, "saldo":saldo, "limite":limite}

def deposito(conta, valor):
    conta["saldo"] += valor

def saque(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("O saldo da conta é: {}".format(conta["saldo"]))