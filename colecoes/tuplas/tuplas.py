# tuplas são imutáveis

# declarando uma tupla
frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)

# ACESSO DIRETO 
print(frutas[0])  # laranja
print(frutas[2])  # uva

# INDICES NEGATIVOS
print(frutas[-1])  # uva
print(frutas[-3])  # laranja
