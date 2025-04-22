print(("ola mundo"))
print(type('ola mundo'))
print(type(3.14))
print(type(2))
print(type(2.5))
print(type(2+3j))
print(type(True))
print(type(False))
print(type([1,8,7,9]))
print(type({1,5,8,7}))
#print(type('2','4',3))


print(type('5'+'2'))
print(type(5+2))

for x in range(11):
    for y in range(11):
        print(f'{x}x{y}={x*y}')


frase1='A LINGUAGEM PYTHON É MUITO FACIL DE APRENDER'
frase1=frase1.lower()

print(frase1.split())

erro='\033[91m'
normal='\033[0m'
print(erro,'mensagem de erro',normal)

tuplacores = ('azul', 'branco', 'azul', 'vermelho', 'preto', 'azul',
'amarelo')
print(tuplacores.count('azul'))