#24) Pedir senha até que seja digitada a correta

senha1 = 1234
senha2 = int(input("Digite sua Senha de 4 dígitos"))
if (senha1 == senha2):
    print("Acesso Liberado!")
else:
    print("Acesso Negeado!")
