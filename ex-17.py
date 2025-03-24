#17) Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.
print("Digite três números distintos.")
valor1 = int(input("Digite o primeiro valor:"))
valor2 = int(input("Digite o segundo valor:"))
valor3 = int(input("Digite o terceiro valor:"))
if(valor1>valor2):
    print(valor1, "é maior que", valor2)
else:
    print(valor2, "é maior que", valor1)
    if(valor1>valor3):
        print(valor1, "é maior que", valor3)
    else:
        print(valor3, "é maior que", valor1)
        if(valor2>valor3):
            print(valor2, "é maior que", valor3)
        else:
            print(valor3, "é maior que", valor2) 
