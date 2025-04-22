import random as rd

lista=["pedra", "papel","tesoura"]

while True:
    humano= input(" Escolha pedra,papel ou tesoura : ")
    computador = rd.choice(lista)

    if humano == computador:
        print(f'humano escolheu: {humano} computador escolheu : {computador}')
        print("empate")
    elif humano=="pedra" and computador=="tesoura":
        print(f'humano escolheu: {humano} computador escolheu : {computador}')
        print("Humano ganhou : ")
    elif humano=="tesoura" and computador=="pedra":
        print(f'humano escolheu: {humano} computador escolheu : {computador}')
        print("Humano perdeu : ")
    elif humano=="pedra" and computador=="papel":
        print(f'humano escolheu: {humano} computador escolheu : {computador}')
        print("Humano ganhou : ")
    elif humano=="papel" and computador=="pedra":
        print(f'humano escolheu: {humano} computador escolheu : {computador}')
        print("Humano perdeu : ")
    elif humano=="tesoura" and computador=="papel":
        print(f'humano escolheu: {humano} computador escolheu : {computador}')
        print("Humano ganhou : ")
    elif humano=="papel" and computador=="tesoura":
        print(f'humano escolheu: {humano} computador escolheu : {computador}')
        print("Humano perdeu : ")
    
    sair = input("sair [n]continuar [y] ")
    if sair=="n":
        break
    else:
        pass