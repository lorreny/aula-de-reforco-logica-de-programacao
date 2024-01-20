## **Condicionais** (if...elif...else)
# O Imposto Nacional Sobre Salários Altíssimos (INSSA) é um imposto que incidi sobre salários superiores a 
# R$ 15.345,73, observando as regras a seguir:
# *   Salários **entre** R$ 15.345,73 e R$ 18.343,73 têm desconto de 4.75%;
# *   Salários **entre** R$ 18.345,73 e R$ 21.343,73 têm desconto de 7.75%;
# *   Salários **entre** R$ 21.345,73 e R$ 24.343,73 têm desconto de 10.75%.
# Faça um algoritmo que verifique:
# *   Se o INSSA incidirá sobre o salário informado pelo usuário;
# *   Qual o percentual de imposto que incidirá sobre o salário, caso se aplique as regras do INSSA;
# *   Qual a diferença do salário bruto (sem o imposto) e do salário líquído (com o imposto);
# *   Qual a representação em dinheiro (R$) do percentual do imposto.
# **Atenção**: desenvolva a atividade na célula de código abaixo.

salario = float(input("Informe o valor do seu salário: "))

if salario >= 21343.73:
    print("O INSSA incidirá sobre o seu salário, o imposto será de 10,75")
    #imposto_em_dinheiro = salario * 0.1075 #Valor do imposto: R$ 5375.0
    #print(f"Valor do imposto: R$ {imposto_em_dinheiro}") 
    porcentagem = (salario * 10.75) / 100
    salario_liquido = salario - porcentagem
    print(f"Valor do imposto: R$ {porcentagem}") 
    print(f"O valor do seu salário bruto é {salario} e o valor do seu salário líquido é {salario_liquido}")
elif salario >= 18345.73 or salario > 21343.73:
    print("valor entre 18 e 20")
    print("O INSSA incidirá sobre o seu salário, o imposto será de 7,75")
    porcentagem = (salario * 7.75) * 100
    salario_liquido = salario - porcentagem
    print(f"Valor do imposto: R$ {porcentagem}") 
    print(f"O valor do seu salário bruto é {salario} e o valor do seu salário líquido é {salario_liquido}")
elif salario >= 15345.73 or salario > 18343.73: #se salario for maior e menor 
    print("valor entre 15 e 18")
    print("O INSSA incidirá sobre o seu salário, o imposto será de 4,75")
    porcentagem = (salario / 4.75) * 100
    salario_liquido = salario - porcentagem
    print(f"Valor do imposto: R$ {porcentagem}") 
    print(f"Valor do imposto: R$ {imposto_em_dinheiro}")
    print(f"O valor do seu salário bruto é {salario} e o valor do seu salário líquido é {salario_liquido}")
else: #elseção
    print(f"O valor informado não se aplica no cálculo do Imposto Nacional sobre Salários Altíssimos")
