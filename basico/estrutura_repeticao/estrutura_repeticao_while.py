opcao = -1

while opcao != 0: #enquanto opcao for diferente de 0 faça:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1: #se opcao igual valor e tipo
        print("Sacando...")
    elif opcao == 2: #condicao 1
        print("Exibindo o extrato...")
else: #senao
    print("Obrigado por usar nosso sistema bancário, até logo!")
