# Definição de Funções
# estrutura de uma função
def saudacao():
    print("Olá, bem-vindo!")
saudacao() #chamando uma função

# Função com Parâmetro
def saudacao(nome):
    print(f"Olá, {nome}!")
saudacao("Elisa")

# Função Lambda
quadrado = lambda x: x ** 2
print(quadrado(5))
