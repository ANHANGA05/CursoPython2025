def minhaFuncao():
        # estrutura condicional
    nome=input("digita o primeiro nome : ")

    if nome=="Yonice":
        print(f'Bem vindo : {nome}')
    else:
        print("O nome esta errado")
        
    nome1=input("digita o segundo nome : ").strip()

    if nome1=="Gomes":
        print(f'Bem vindo : {nome1}')
    else:
        print("O nome esta errado")

print(minhaFuncao())