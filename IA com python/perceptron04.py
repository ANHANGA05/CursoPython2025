#Solução da XOR

def step(x):
    return 1 if x >= 0 else 0

# Perceptrons básicos
def nand(x1, x2):
    return step(-x1 - x2 + 1.5)

def or_(x1, x2):
    return step(x1 + x2 - 0.5)

def and_(x1, x2):
    return step(x1 + x2 - 1.5)

# MLP simulado para XOR
def xor_mlp(x1, x2):
    h1 = nand(x1, x2)  # Neurônio oculto 1
    h2 = or_(x1, x2)   # Neurônio oculto 2
    out = and_(h1, h2) # Neurônio de saída
    return out
for x1, x2 in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    print(f"{x1} XOR {x2} = {xor_mlp(x1, x2)}")
