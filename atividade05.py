a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
formula = b**2-4*a*c

if formula > 0:
    print("Existem duas raizes reais distintas.")
elif formula == 0:
    print("Existem duas raizes reais iguais.")
elif formula < 0:
    print("Existem duas raizes imaginárias conjungadas.")