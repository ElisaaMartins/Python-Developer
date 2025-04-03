while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break #para o laço

    if numero % 2 == 0:
        continue #continua o laço

    print(numero)


# for numero in range(100):

#     if numero % 2 == 0:
#         continue

#     print(numero, end=" ")
