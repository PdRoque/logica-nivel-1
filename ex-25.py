#25) Somar números positivos digitados pelo usuário até que ele digite um número negativo.

soma = 0

for x in range(100):
    numero = int(input("Digite valores positivos (ou negativos para parar a soma)"))
    
    if numero < 0:
        break #se for negativo sai do loop
    soma += numero
print(f"A soma dos valores positivos é:{soma}")
