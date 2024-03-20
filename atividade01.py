idade = int(input("Seja bem vindo(a) ao Hopi Hari!! por favor nos informe sua idade em kg: "))
peso = float(input("Agora, por favor nos informe seu peso em metros: "))

if idade > 15 and peso <= 120:
    print(("Tenha um bom passeio!!"))
elif idade <= 15 or peso > 120:
    print(("Sentimos muito, mas seu peso e/ou sua altura estão fora dos parametros permitidos pela montanha russa."))