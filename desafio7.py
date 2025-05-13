
import random   

print("Olá, Você está no Banco JWC!")

Titular_da_conta = ("Leonardo Gomes", "Joao Ferreira", "Luis Salomao", "Vitor Azevedo")
Agencia = ()
Conta_Corrente = ()
Saldo = []
Saque = []

Agencia = int(input("Agencia: "))
Conta_Corrente = int(input("Conta Corrente: "))
Titular_da_conta = random.choice(Titular_da_conta)
str(input(Titular_da_conta))

print(50*"-")
print("Qual operação vai realizar?")
while True:
    menu = int(input("\nPara depósito - 1 \nPara saque - 2 \nPara consultar Saldo - 3 \nPara consultar seu extrato - 4 \nDigite aqui: "))

    if menu == 1:
        deposito = float(input("Depósito: "))
        if deposito <= 0:
            deposito = 0
            print("Valor inválido, digite corretamente")
        else:
            Saldo[0] += deposito
            print("Informe o valor do seu depósito: R$ {}".format(deposito))
    elif menu == 2:
        if Saque <= 0:
            print("Valor inválido")
        else:
            Saldo -= Saque

