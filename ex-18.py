#18) Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.

# leitura dos 3 valores
print("Digite três números distintos.")
x = int(input("Digite o primeiro valor:"))
y = int(input("Digite o segundo valor:"))
z = int(input("Digite o terceiro valor:"))

valores = [x, y, z] # organizando valores
valores.sort() # ordena os valores em ordem crescente

soma_valores = valores[1] + valores[2] # soma dos maiores
print("A soma dos 2 maiores valores é:",soma_valores)
