nome = "gUIlherME"

print(nome.upper()) #maiusculo
print(nome.lower()) #minusculo
print(nome.title()) #primeira letra maiuscula

texto = "  Olá mundo!    "

print(texto + ".")
print(texto.strip() + ".") #remove os espaços em branco no começo e no final
print(texto.rstrip() + ".") #remove os espaços em branco no final
print(texto.lstrip() + ".") #remove os espaços em branco no começo

menu = "Python"

print("####" + menu + "####") 
print(menu.center(14)) #da um espaço de 14pxs e coloca no meio
print(menu.center(14, "#")) #da um espaço de 14pxs e coloca #
print("-".join(menu)) #separa a palavra com o que foi definido

# PRINT COM RECUOS DIFERENTES
nome = "Guilherme"

mensagem = f"""
   Olá meu nome é {nome},
 Eu estou aprendendo Python.
     Essa mensagem tem diferentes recuos.
"""

print(mensagem)