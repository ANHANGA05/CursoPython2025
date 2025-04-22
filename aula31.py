#Argumento posicionais

def exibir_preco(nome_produto, preco):
    print(F'produto {nome_produto} preço {preco}')


exibir_preco(200, "HP")# errado
exibir_preco("HP", 2000)# certo 
exibir_preco(preco=20000, nome_produto="lenovo")# Certo