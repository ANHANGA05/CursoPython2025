# calcular media dos alunos
num1 = float(input("Digite o primeiro número entre 0 e 20: "))

if not (0 <= num1 <= 20):  # Se o número estiver fora do intervalo
    num1 = float(input("Número inválido. Digite novamente um número entre 0 e 20: "))

if 0 <= num1 <= 20:  # Agora, verificamos novamente para garantir que seja válido
    num2 = float(input("Digite o segundo número entre 0 e 20: "))
    
    if 0 <= num2 <= 20:
        media = (num1 + num2) / 2
        print(f"A média entre {num1} e {num2} é {media:.2f}")
    else:
        print("O segundo número está fora do intervalo.")
else:
    print("O primeiro número ainda está inválido. Programa encerrado.")

