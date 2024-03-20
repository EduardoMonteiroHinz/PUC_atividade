print("Se seu genero for masculino digite 1\nMulher digite 2")
sexo = int(input("Qual é o seu sexo? "))
h = float(input("Informe a sua altura: "))

formulah = (72.7*h)-58
formulam = (62.1*h)-44.7

if sexo == 1:
    print(f"Seu peso ideal é igual a: {formulah}")
elif sexo == 2:
    print(f"Seu peso ideal é igual a: {formulam}")