# 19) Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.

# Passo 1: Leitura dos três valores
print("Digite 3 valores distintos:")
x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
z = int(input("Digite o terceiro valor: "))

valores = [x, y, z]
valores.sort()  # Ordena os valores em ordem crescente
print(valores)
