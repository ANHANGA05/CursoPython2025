# funcao com retorno com dois argumento

def minhaFuncao(x, y):
    return(x*y)

c=minhaFuncao(2,2)

print(c)

# De outra forma mas usando variavel global
def minhaFuncao01(x, y):
    global z
    z=x*y
    return(c)

minhaFuncao01(2,2)

print(f' valor retornado é :  {z} ')

