# vamos solicitar omo entrada, um número inteiro e verifique se ele é par ou ímpar. 

num = int(input("Digite um número inteiro: "))  

# Verificando se o número é par ou ímpar
if num % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")      

# Vamos solicitar como entrada dois números e depois vamos verificar se eles são pares ou ímpares.
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))          

# Verificando se os números são pares ou ímpares
if num1 % 2 == 0:
    print(f"O primeiro número ({num1}) é par.")
else:
    print(f"O primeiro número ({num1}) é ímpar.")       

if num2 % 2 == 0:
    print(f"O segundo número ({num2}) é par.")
else:
    print(f"O segundo número ({num2}) é ímpar.")    

