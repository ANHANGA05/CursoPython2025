import numpy as np

class Perceptron:
    def __init__(self, n_inputs, threshold=0.5):
        self.weights = np.random.randn(n_inputs)  # Inicializa pesos aleatórios
        self.threshold = threshold  # Limiar (threshold)

    def predict(self, inputs):
        # Calcula a soma ponderada das entradas
        weighted_sum = np.dot(inputs, self.weights)
        # Aplica a função de ativação (limiar)
        return 1 if weighted_sum > self.threshold else 0

    def train(self, training_inputs, labels, epochs=10, learning_rate=0.1):
        for _ in range(epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                # Atualiza os pesos com base no erro
                self.weights += learning_rate * error * inputs

# Conjunto de dados de entrada (Exemplo simples)
entradas = np.array([[1.5, 2.3, -1.2], [1.0, 1.5, -0.8], [0.5, 1.8, -0.5], [2.2, 3.1, -1.0]])
labels = np.array([1, 0, 0, 1])  # Labels esperados

# Criando o modelo Perceptron
perceptron = Perceptron(n_inputs=3)

# Treinando o modelo
perceptron.train(entradas, labels, epochs=10)

# Testando o modelo com as entradas
for entrada in entradas:
    print(f"Entrada: {entrada}, Predição: {perceptron.predict(entrada)}")
