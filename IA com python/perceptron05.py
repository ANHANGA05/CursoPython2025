#entrada de dados
import numpy as np

# Conjunto de Dados de Entrada (Vetor de Atributos)
entradas = np.array([[150, 7.5],  # Maçã
                     [120, 6.2],  # Pera
                     [200, 8.0],  # Maçã
                     [180, 7.0]]) # Pera

# Rótulos de Saída (Labels)
labels = np.array([1, 0, 1, 0])  # 1 = Maçã, 0 = Pera

# Exemplo de modelo Perceptron com entrada de dados e treinamento
class Perceptron:
    def __init__(self, n_inputs, learning_rate=0.1):
        self.weights = np.zeros(n_inputs)  # Inicializa os pesos
        self.bias = 0  # Inicializa o viés
        self.learning_rate = learning_rate  # Taxa de aprendizado

    def predict(self, inputs):
        # Calcula a soma ponderada e aplica a função de ativação (passo)
        weighted_sum = np.dot(inputs, self.weights) + self.bias
        return 1 if weighted_sum >= 0 else 0

    def train(self, training_inputs, labels, epochs=10):
        for _ in range(epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                self.weights += self.learning_rate * error * inputs
                self.bias += self.learning_rate * error

# Criando o modelo Perceptron com 2 entradas
perceptron = Perceptron(n_inputs=2)

# Treinando o modelo com as entradas e rótulos
perceptron.train(entradas, labels, epochs=10)

# Testando o modelo
for entrada in entradas:
    print(f"Entrada: {entrada}, Predição: {perceptron.predict(entrada)}")

