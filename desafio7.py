import random   

print("Olá, Você está no Banco JWC!")

titular_da_conta = ("Leonardo Gomes", "Joao Ferreira", "Luis Salomao", "Vitor Azevedo")
agencia = ()
conta_corrente = ()
saldo = [0]
saque = []
historico = []


agencia = int(input("Agencia: "))
conta_corrente = int(input("Conta Corrente: "))
titular_da_conta = random.choice(titular_da_conta)
str(input(titular_da_conta))

controle = True

print(50*"-")
print("Qual operação vai realizar?")

while controle == True:
    menu = int(input("\nPara depósito - 1 \nPara saque - 2 \nPara consultar Saldo - 3 \nPara consultar seu extrato - 4 \nDigite aqui: "))

    if menu == 1:
        deposito = float(input("Depósito: "))
        if deposito <= 0:
            deposito = 0
            print("Valor inválido, digite corretamente")
        else:
            saldo[0] += deposito
            print("Você depositou: R$ {}".format(deposito))
            historico.append(deposito)

    elif menu == 2:
        saque = float(input("Qual o valor do saque?"))
        if saque <= 0:
            print("Valor inválido")
        elif saldo[0] == 0:
            print("Saldo insuficiente!")
        elif saque > saldo [0]:
            print("Saldo insuficiente")
        else:
            saldo[0] = saldo[0] - saque
            print("Saque de R$ {} realizado".format(saque))
            historico.append(-saque)
    elif menu == 3:
        print("Saldo atualizado: R$ {}".format(saldo))
    elif menu == 4:
        print("Olhe seu extrato: {}".format(historico))
    else:
        controle == False
        print("Volte sempre Sr(a). {}".format(titular_da_conta))
        break
