texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável
for letra in texto: #enquanto letra estiver em texto faça:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
# enquanto numero estiver na confição do range faça:
for numero in range(0, 51, 5): #gera números de 0 até 50, pulando de 5 em 5
    print(numero, end=" ")
