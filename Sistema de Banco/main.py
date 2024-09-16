#> Autor: Kauã Lima
#> Data: 16/09/2024

#> Desafio Sistema Bancário
#| Fomos contratados por um grande banco para desenvolver seu novo sistema.
#| Esse banco deseja modernizar suas operações e para isso escolheu a linguargem Python.
#| Para a primeira versão do sistema, devemos implementar apenas 3 operações: depósito, saque e extrato.

#> Definições gerais
saldo = 0
limite = 500
extrato = ""
cont_saques = 0
numero_saques = 0
LIMITE_SAQUES = 3

#> Subprogramas
def verifica_saldo(saldo, valor):
    if saldo < valor:
        return False
    
    else: 
        return True

#> Saque
#| O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
#| Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será
#| possível sacar o dinheiro por falta de saldo.
#| Todos os saques deve mser armazenados em uma variável e exibidos na operação de extrato.
def sacar(cont_saques, saldo, valor, limite_saques, extrato, verifica_saldo):
    valida_saldo = verifica_saldo(saldo, valor)

    if cont_saques >= 3:
        return print("Você já atingiu o seu limite de saques hoje!")
    
    elif valor > limite_saques:
        return print("O seu limite de saque diário é de R$ 500.00. Realize a operação novamente.")
    
    elif valida_saldo:
        saldo -= valor

        extrato += f"[Saque] - R$ {valor} / Saldo pós-saque: R$ {saldo}\n"

        print(f"Você sacou R$ {valor} com sucesso!")

        return cont_saques + 1, saldo, extrato
    
    else:
        print("Você não possui saldo suficiente para o saque. Realize a operação novamente.")

        return cont_saques, saldo, extrato
    
#> Depósito
#| Deve ser possível depositar valores positivos para a minha conta bancária.
#| A v1 do projeto trabalha apenas com 1 usuário, dessa forma, não precisamos nos preocupar em
#| identificar qual é o número da agência e conta bancária.
#| Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor

        extrato += f"[Depósito] + R$ {valor} / Saldo pós-depósito: R$ {saldo}\n"

        print(f"Você depositou R$ {valor} com sucesso!")

        return saldo, extrato

    else:
        print("Você não possui saldo suficiente para o saque. Realize a operação novamente.")

        return saldo, extrato

#> Extrato
#| Essa operação deve listar todos os depósitos e saques realizados na conta.
#| No fim deve ser exibido o saldo atual da conta.
#| Os valores devem ser exibidos utilizando o formato: R$ XXXX.XX, exemplo: R$ 1500.45
def exibir_extrato(extrato, saldo):
    return print(f"{extrato}\nSaldo atual: R$ {float(saldo)}")

#> Menu
menu = """
    Bem-vindo(a)!
    Escolha a opção que deseja visitar.
    [0] Sair do programa
    [1] Realizar depósito
    [2] Realizar saque
    [3] Extrato
"""

while True:

    opcao = int(input(f"{menu} Resposta: "))

    if opcao == 0:
        break

    elif opcao == 1:
        valor = float(input("\nQuanto deseja depositar?\n Resposta: "))
        
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == 2:
        valor = float(input("\nQuanto deseja sacar?\n Resposta: "))

        cont_saques, saldo, extrato = sacar(cont_saques, saldo, valor, limite, extrato, verifica_saldo)

    elif opcao == 3:
        exibir_extrato(extrato, saldo)