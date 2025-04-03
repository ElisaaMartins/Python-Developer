menu = """      

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """          #o que o usuário vai esolher

saldo = 0       #saldo inicial
limite = 500    #limite do saldo
extrato = ""    #extrato erado pq vai do que o usuario vai colocar
numero_saques = 0   
LIMITE_SAQUES = 3   #só pode sacar 3vezes - constante

while True: #enquanto for verdadeiro, faça:

    opcao = input(menu) #o usuario escolhe

    if opcao == "d": #se a opção for d
        valor = float(input("Informe o valor do depósito: ")) 

        if valor > 0: #se valor maior que 0
            saldo += valor #soma
            extrato += f"Depósito: + R$ {valor:.2f}\n" #printa o extrato

        else: #senão falha
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s": #se for s
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo #se passar do saldo inicial

        excedeu_limite = valor > limite #se passar do limite de saldo

        excedeu_saques = numero_saques >= LIMITE_SAQUES #se passar do limite dos saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0: #condição: valor do saque maior que 0
            saldo -= valor #tira o valor do saldo
            extrato += f"Saque: - R$ {valor:.2f}\n" 
            numero_saques += 1 #contagem de saques

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e": #condição: mostra o extrato com e
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato) #se não teve extrato nenhum
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
