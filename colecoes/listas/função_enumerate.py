# as vezes é necessario saber qual o indice do objeto dentro do laço for. Para isso usamos a função enumerate
carros = ["gol", "celta", "palio"]
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}") 
