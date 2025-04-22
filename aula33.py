# argumerntos dinamicos nomeados

def somar (*a):
    return a

print(somar(2,5,8,))



def somar (*a):
    for valor in a:
        print(valor)

print(2,5,8,8,77,55,11,44,77,87)


def mostrar(**a):
    print(a)

mostrar(a=1,b=2,c=8)

def mostrar(**a):
    for valor in a.values():
        print(a)

mostrar(a=1,b=2,c=8)

def demostrar(*args,**kwargs):
    print(args)
    print(kwargs)

demostrar(1,2,4,5,4,a=1, b=4,c=8)
