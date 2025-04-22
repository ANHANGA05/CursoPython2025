tentativas = 3

entrada = input("Digite um número: ")

if entrada.lstrip('-').isdigit():
    numero = int(entrada)
    if numero > 0:
        print("O número digitado é positivo.")
    elif numero < 0:
        print("O número digitado é negativo.")
    else:
        print("O número digitado é zero.")
else:
    tentativas -= 1
    if tentativas > 0:
        print(f"Entrada inválida! Você tem {tentativas} tentativas restantes.")
        entrada = input("Digite um número: ")
        
        if entrada.lstrip('-').isdigit():
            numero = int(entrada)
            if numero > 0:
                print("O número digitado é positivo.")
            elif numero < 0:
                print("O número digitado é negativo.")
            else:
                print("O número digitado é zero.")
        else:
            tentativas -= 1
            if tentativas > 0:
                print(f"Entrada inválida! Você tem {tentativas} tentativas restantes.")
                entrada = input("Digite um número: ")
                
                if entrada.lstrip('-').isdigit():
                    numero = int(entrada)
                    if numero > 0:
                        print("O número digitado é positivo.")
                    elif numero < 0:
                        print("O número digitado é negativo.")
                    else:
                        print("O número digitado é zero.")
                else:
                    print("Você excedeu o número de tentativas.")
            else:
                print("Você excedeu o número de tentativas.")
