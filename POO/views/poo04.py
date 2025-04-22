class Usuario:
    def __init__(self,nome,idade):# 
        self.nome=nome
        self.idade=idade
    
    def Boas_Vindas(self):
        print(f'Usuário: {self.nome}, Idade: {self.idade}')

usuario1 = Usuario(nome='Fernando', idade='31')
usuario1.Boas_Vindas()
print(usuario1.nome)
