#13 - Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.
idade = int(input("Qual é a sua idade em anos?"))
print("sua idade em meses é:")
print(idade*12)
print("sua idade em dias é:")
print(365 * idade)
