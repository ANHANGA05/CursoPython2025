# Revisão sobre funções


# funções simples
def boas_vindas():
    print('Olá, seja bem vindo ao meu programa!!!')
    print('Espero que você tenha uma boa experiência...')

print(boas_vindas())

#Função composta, com parâmetros
def eleva_numero_ao_cubo(num):
    valor_a_retornar = num * num * num
    return(valor_a_retornar)

num = eleva_numero_ao_cubo(5)
print(num)

#Função composta, com *args e **kwargs
def print_2_vezes(*args):
    for parametro in args:
        print(parametro + '!' + parametro + '!')

print_2_vezes('Olá Mundo!!! ')

def informacoes(**kwargs):
    for dado, valor in kwargs.items():
        print(dado + '-' + str(valor))
        
informacoes(nome='Fernando', idade=30,
nacionalidade='Brasileiro')
