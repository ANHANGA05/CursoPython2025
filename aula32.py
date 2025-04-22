# argumerntos dinamicos

def somar (*a,b):
    print(a)

somar(2,5,8,b=0)


def somar (*a,b):
    for x in a:
        print(x)
    print(b)

somar(2,5,77,8,9,10,8,b=100)