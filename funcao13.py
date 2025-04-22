

def minhaFuncao(x, y):
    global c
    c=x*y
    return(c)

minhaFuncao(2,2)

print(f'O valor retornado é :  {c} ')

# O melhor é sem variavel global

def minhaFuncao(x, y):
    global c
    c=x*y
    return(c)

resultado=minhaFuncao(2,2)

print(f'O valor retornado é :  {resultado} ')