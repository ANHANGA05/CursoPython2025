# Solicita e valida a primeira nota
nota1 = float(input("Digite a primeira nota entre 0 e 20: "))
if nota1 >= 20:
    nota1 = float(input("Nota inválida. Digite novamente a primeira nota entre 0 e 20: "))
    if  nota1 >= 20:
        nota1 = float(input("Última tentativa! Digite a primeira nota entre 0 e 20: "))

# Se a primeira nota ainda for inválida, o programa encerra
if nota1 >= 20:
    print("Você excedeu o número de tentativas. Programa encerrado.")
    exit()