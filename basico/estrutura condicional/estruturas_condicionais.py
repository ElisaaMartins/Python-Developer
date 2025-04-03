MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE: #se idade maior ou igual a maior_idade
    print("Maior de idade, pode tirar a CHN.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE: #se idade maior ou igual a maior_idade
    print("Maior de idade, pode tirar a CHN.")
else: #senão 
    print("Ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE: #se idade maior ou igual a maior_idade
    print("Maior de idade, pode tirar a CHN.")
elif idade == IDADE_ESPECIAL: #condição 1
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else: #senão
    print("Ainda não pode tirar a CNH.")
