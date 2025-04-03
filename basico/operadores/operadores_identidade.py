# como se fosse comparação de conjuntos - está ou não está contido
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso) #curso está em nome_curso
print(saldo is limite) #saldo está em limite
print(saldo is not limite) #saldo não está em limite
