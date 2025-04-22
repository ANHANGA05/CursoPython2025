import random # gerar numero o lista aleatoria
import time   # tempo de espera

def minhaFuncao():
 
    d=random.random()
    print(d)
    d1=random.random()
    print(d1)
    d2=random.randint(1,10)
    print(d2)

    num1=int(input("digita um Numero de 1 a 10 : " ))
    num2=random.randint(1,10)
    print(f'o Humano escolheu : {num1} o computador escolheu : {num2}')

    lista=["pedra ","papel ","tesoura"]
    num3=random.choice(lista)
    print(num3)

    num4=str(input("digita pedra, papel ou tesoura: " ))
    time.sleep(3)
    lista1=["pedra ","papel ","tesoura"]
    num5=random.choice(lista1)
    print(f'o Humano escolheu : {num4} o computador escolheu : {num5}')

# Chamar a funcao.
print(minhaFuncao())