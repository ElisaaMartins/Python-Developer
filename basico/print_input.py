#INPUT - metodo que pede para o usuario inserir uma informação
nome = input("Informe o seu nome: ") #guarda na variavel
idade = input("Informe a sua idade: ")

print(nome, idade)
print(nome, idade, end="...\n")  #\n - quebra de linha
print(nome, idade, sep="#", end="...\n") #end - finaliza a linha com o que foi definido
print(nome, idade, sep="#") #sep - separa os argumentos com o que foi definido
