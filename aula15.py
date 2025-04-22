# Solicita e valida a primeira nota
nota1 = float(input("Digite a primeira nota entre 0 e 20: "))
if not (0 <= nota1 <= 20):
    nota1 = float(input("Nota inválida. Digite novamente a primeira nota entre 0 e 20: "))

# Solicita e valida a segunda nota
if 0 <= nota1 <= 20:  # Só continua se a primeira nota for válida
    nota2 = float(input("Digite a segunda nota entre 0 e 20: "))
    if not (0 <= nota2 <= 20):
        nota2 = float(input("Nota inválida. Digite novamente a segunda nota entre 0 e 20: "))

# Solicita e valida a terceira nota
if 0 <= nota1 <= 20 and 0 <= nota2 <= 20:  # Só continua se as duas primeiras notas forem válidas
    nota3 = float(input("Digite a terceira nota entre 0 e 20: "))
    if not (0 <= nota3 <= 20):
        nota3 = float(input("Nota inválida. Digite novamente a terceira nota entre 0 e 20: "))

# Calcula e exibe a média se todas as notas forem válidas
if 0 <= nota1 <= 20 and 0 <= nota2 <= 20 and 0 <= nota3 <= 20:
    media = (nota1 + nota2 + nota3) / 3
    print(f"A média das notas {nota1}, {nota2} e {nota3} é {media:.2f}")
else:
    print("Uma das notas continua inválida. Programa encerrado.")
