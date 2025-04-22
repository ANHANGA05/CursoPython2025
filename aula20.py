tentativas = 3

for _ in range(tentativas):
    entrada = input("Digite um número: ")
    
    if entrada.lstrip('-').isdigit():
        numero = int(entrada)
        if numero > 0:
            print("O número digitado é positivo.")
        elif numero < 0:
            print("O número digitado é negativo.")
        else:
            print("O número digitado é zero.")
        break
    else:
        print("Entrada inválida! Por favor, digite apenas números e não letras.")
else:
    print("Você excedeu o número de tentativas.")
