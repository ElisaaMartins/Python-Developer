# CRIANDO SETS
# um set é uma coleção que não possui objetos repetidos
# representam conjuntos matematicos ou eliminam itens duplicados de um iteravel

set([1, 2, 3, 1, 3, 4])  #  {1, 2, 3, 4}

set("abacaxi") # {'a', 'b', 'c', 'x', 'i'}

set(("palio", "gol", "celta", "palio")) # {'palio', 'gol', 'celta'}

"""
conjuntos não suportam a indexação ou fatiamento, por isso para acessar seus valores é necessario
convertê-los para listas
"""
numeros = {1, 2, 3, 2}
numeros = list(numeros)

print(numeros[0])

