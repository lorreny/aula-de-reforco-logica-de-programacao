#Crie um algoritimo que vai imprimir a tabuada até 10
for i in range(11):
    for num in range(11):
        resultado = i * num
        print(f"{i} * {num} = {resultado}")

num = int(input("Informe 1 numero para fazermos a tabuada: "))
for i in range(11):
    resultado = i * num
    print(f"{i} * {num} = {resultado}")
