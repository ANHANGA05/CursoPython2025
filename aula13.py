# calcular media dos alunos
p1=int(input("Escreva a sua primeira nota1 : "))
p2=int(input("Escreva a sua segunda nota2 : "))
p3=int(input("Escreva a sua terceira nota3 : "))


media=(p1+p2+p3)/3
if media<=20:
    print(f'A sua media é : {media}')
    if media>=10:
        print("Voce esta Aprovado")
    else:
        print("Voce esta Reprovado")
else:
    print(" O valor da media tem que ser 0 a 20")
