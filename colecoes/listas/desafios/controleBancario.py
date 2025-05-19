'''
ENTRADA
Uma lista contendo valores inteiros ou decimais representando as transações realizadas (ex.: [100, -50, 200]).
Valores positivos representam depósitos.
Valores negativos representam saques.

SAÍDA
O saldo final da conta no formato: "Saldo: R$ X.XX"
'''

''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''


def calcular_saldo(transacoes):
    saldo = 0

    #TOdo Itere sobre cada transação na lista:
    for transacao in transacoes:
        # TOdo: Adicione o valor da transação ao saldo
        saldo += transacao

    # TOdo: Retorne o saldo formatado em moeda brasileira com duas casas decimais:
    return f"Saldo: R$ {saldo:.2f}"

entrada_usuario = input()

entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# TOdo: Calcule o saldo com base nas transações informadas:
resultado = calcular_saldo(transacoes)

print(resultado)