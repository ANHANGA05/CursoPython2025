# Função de ativação (degrau)
def step(x):
    return 1 if x >= 0 else 0

# Porta NOT (1 entrada)
def perceptron_not(x):
    w = -1.0
    b = 0.5
    return step(w * x + b)

# Porta AND
def perceptron_and(x1, x2):
    w1, w2 = 1.0, 1.0
    b = -1.5
    return step(x1 * w1 + x2 * w2 + b)

# Porta OR
def perceptron_or(x1, x2):
    w1, w2 = 1.0, 1.0
    b = -0.5
    return step(x1 * w1 + x2 * w2 + b)

# Porta NAND (negado do AND)
def perceptron_nand(x1, x2):
    w1, w2 = -1.0, -1.0
    b = 1.5
    return step(x1 * w1 + x2 * w2 + b)

# Porta XOR (montada com perceptrons NAND, OR e AND)
def perceptron_xor(x1, x2):
    nand = perceptron_nand(x1, x2)
    or_ = perceptron_or(x1, x2)
    return perceptron_and(nand, or_)

# Testando as portas
entradas = [(0, 0), (0, 1), (1, 0), (1, 1)]

print("PORTA NOT:")
for x in [0, 1]:
    print(f"NOT({x}) = {perceptron_not(x)}")

print("\nPORTA AND:")
for x1, x2 in entradas:
    print(f"{x1} AND {x2} = {perceptron_and(x1, x2)}")

print("\nPORTA OR:")
for x1, x2 in entradas:
    print(f"{x1} OR {x2} = {perceptron_or(x1, x2)}")

print("\nPORTA NAND:")
for x1, x2 in entradas:
    print(f"{x1} NAND {x2} = {perceptron_nand(x1, x2)}")

print("\nPORTA XOR (usando combinação de perceptrons):")
for x1, x2 in entradas:
    print(f"{x1} XOR {x2} = {perceptron_xor(x1, x2)}")
