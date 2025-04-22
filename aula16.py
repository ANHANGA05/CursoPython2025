# Solicita e valida a primeira nota
nota1 = float(input("Digite a primeira nota entre 0 e 20: "))
if not (0 <= nota1 <= 20):
    nota1 = float(input("Nota inválida. Digite novamente a primeira nota entre 0 e 20: "))
    if not (0 <= nota1 <= 20):
        nota1 = float(input("Última tentativa! Digite a primeira nota entre 0 e 20: "))

# Se a primeira nota ainda for inválida, o programa encerra
if not (0 <= nota1 <= 20):
    print("Você excedeu o número de tentativas. Programa encerrado.")
    exit()

# Solicita e valida a segunda nota
nota2 = float(input("Digite a segunda nota entre 0 e 20: "))
if not (0 <= nota2 <= 20):
    nota2 = float(input("Nota inválida. Digite novamente a segunda nota entre 0 e 20: "))
    if not (0 <= nota2 <= 20):
        nota2 = float(input("Última tentativa! Digite a segunda nota entre 0 e 20: "))

# Se a segunda nota ainda for inválida, o programa encerra
if not (0 <= nota2 <= 20):
    print("Você excedeu o número de tentativas. Programa encerrado.")
    exit()

# Solicita e valida a terceira nota
nota3 = float(input("Digite a terceira nota entre 0 e 20: "))
if not (0 <= nota3 <= 20):
    nota3 = float(input("Nota inválida. Digite novamente a terceira nota entre 0 e 20: "))
    if not (0 <= nota3 <= 20):
        nota3 = float(input("Última tentativa! Digite a terceira nota entre 0 e 20: "))

# Se a terceira nota ainda for inválida, o programa encerra
if not (0 <= nota3 <= 20):
    print("Você excedeu o número de tentativas. Programa encerrado.")
    exit()

# Calcula e exibe a média
media=(nota1+nota2+nota3)/3
if media<=20:
    print(f'A sua media é : {media}')
    if media>=10:
        print("Voce esta Aprovado")
    else:
        print("Voce esta Reprovado")
else:
    print(" O valor da media tem que ser 0 a 20")

