class Carro:
    carro1 = 'Gol modelo 2016 completo'
    carro2 = 'Celta ano 2015 4 portas'
    carro3 = 'Uno ano 2015 baixa quilometragem'
    carro4 = 'Clio 2018 flex doc vencido'

print(Carro.carro1)
print(Carro.carro2)

class Pessoa:
    
    pass
pessoa1 = Pessoa()
pessoa1.nome = 'Fernando'
pessoa1.idade = 32

print(pessoa1.nome)
print(pessoa1.idade)


class Pessoa:
    def acao1(self):
        print('Ação 1 está sendo executada...')
pessoa1 = Pessoa()
pessoa1.acao1()

