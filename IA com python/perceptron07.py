import numpy as np

class Perceptron:
    def __init__(self, weights, threshold):
        # Inicializa os pesos e o limiar (threshold)
        self.weights = np.array(weights)
        self.threshold = threshold

    def predict(self, inputs):
        # Calcula a soma ponderada das entradas
        weighted_sum = np.dot(inputs, self.weights)
        # Aplica a função de ativação (limiar)
        if weighted_sum > self.threshold:
            return 1  # Jogar tênis
        else:
            return 0  # Não jogar tênis

# Definindo as entradas e os pesos
entradas = np.array([1, 1, 0])  # [tempo bom, está ventando, bom humor]
pesos = [3, 1, 5]  # Pesos correspondentes
limiar = 5  # Threshold

# Criando o Perceptron
perceptron = Perceptron(pesos, limiar)

# Predição: o que o Perceptron decide com base nas entradas?
resultado = perceptron.predict(entradas)

# Exibindo o resultado
if resultado == 1:
    print("Você joga tênis hoje!")
else:
    print("Você não joga tênis hoje.")
