#Vamos testar se uma palavra da entrada do usuario é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

palavra = input("Digite uma palavra: ")     

# Verificando se a palavra é um palíndromo
if palavra == palavra[::-1]:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")

