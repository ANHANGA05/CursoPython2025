import numpy as np

# Função de ativação degrau (step function)
def step_function(x):
    return 1 if x >= 0 else 0

# Perceptron simples
def perceptron(x1, x2):
    # Pesos e bias
    w1, w2 = 1.0, 1.0
    bias = -1.5

    # Soma ponderada
    weighted_sum = x1 * w1 + x2 * w2 + bias

    # Aplica função de ativação
    return step_function(weighted_sum)

# Testando todas as entradas da porta AND
entradas = [(0, 0), (0, 1), (1, 0), (1, 1)]

print("Simulação da porta AND com Perceptron:")
for x1, x2 in entradas:
    saida = perceptron(x1, x2)
    print(f"Entrada: ({x1}, {x2}) → Saída: {saida}")
