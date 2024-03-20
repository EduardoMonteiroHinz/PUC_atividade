print("PUCPR - 1")
print("UNICAMP - 2")
uni = int(input("Digite o respectivo número da sua faculdade: "))
n1 = float(input("Qual a sua primeira nota? "))
n2 = float(input("Qual a sua segunda nota? "))
media = (n1+n2)/2
if uni == 1:
    if media >= 7:
        print("Aprovado")
    elif 4 <= media < 7:
        print("Recuperação")
    else:
        print("Reprovado")
elif uni == 2:
    if media >= 5:
        print ("Aprovado")
    else: 
        print("Reprovado")
else: 
    print ("ERRO")