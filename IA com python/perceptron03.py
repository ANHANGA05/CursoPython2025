# erro classico da porta XOR
def step(x):
    return 1 if x >= 0 else 0

# Tentativa de simular XOR com 1 perceptron
def perceptron_xor_fail(x1, x2):
    # Escolhendo qualquer combinação de pesos/bias
    w1, w2 = 1.0, 1.0
    b = -1.0
    return step(x1 * w1 + x2 * w2 + b)

# Testando
entradas = [(0, 0), (0, 1), (1, 0), (1, 1)]

print("Tentativa de XOR com único perceptron:")
for x1, x2 in entradas:
    y = perceptron_xor_fail(x1, x2)
    print(f"{x1} XOR {x2} = {y}")
