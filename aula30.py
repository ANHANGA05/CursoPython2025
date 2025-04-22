def soma(a, b):
    c=a+b
    return c
    

def sub(a, b):
    c=a-b
    return c

def mult(a, b):
    c=a*b
    return c

a=int(input("escreva um numero "))
b=int(input("escreva um numero "))

print(f'Primero : {a}  Segundo : {b}')

print(f'Soma do numero é: {soma(a,b)}')
print(f'Subtração do numero é: {sub(a,b)}')
print(f'Multiplicação do numero é: {mult(a,b)}')


