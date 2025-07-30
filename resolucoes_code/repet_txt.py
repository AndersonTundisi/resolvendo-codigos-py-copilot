# Agora vamos solicitar uma string do usuário e depois solicatar a quantidade de vezes que texto será repetido!

texto = input("Digite um texto: ") + " "
repeticoes = int(input("Quantas vezes você quer repetir o texto? ")) 

# Repetindo o texto
texto_repetido = texto * repeticoes     

# Exibindo o resultado
print("Texto repetido:", texto_repetido)    
