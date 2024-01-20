
#https://colab.research.google.com/drive/1fyDbqpzykRIP4LavGr2rpc6nL5bT_Ok6#scrollTo=6sRRj1ZvAABf

salario = float(input("Insira seu salário: "))

if salario <= 15345.73:
    print("Não aplicará imposto.")
    imposto = "0%"
    imposto_em_dinheiro = salario * 0
    salario_liquido = salario - imposto_em_dinheiro
elif salario > 15345.73 and salario <= 18343.73:
    imposto = "4.75%"
    imposto_em_dinheiro = salario * 0.0475
    salario_liquido = salario - imposto_em_dinheiro

elif salario > 18343.73 and salario <= 21343.73:
    imposto = "7.75%"
    imposto_em_dinheiro = salario * 0.0775
    salario_liquido = salario - imposto_em_dinheiro

elif salario > 21343.73:
    imposto = "10.75%"
    imposto_em_dinheiro = salario * 0.1075
    salario_liquido = salario - imposto_em_dinheiro

print(f"O imposto será de {imposto}")
print(f"Valor do imposto: R${imposto_em_dinheiro}")
print(f"Salário líquido: R${salario_liquido}")
