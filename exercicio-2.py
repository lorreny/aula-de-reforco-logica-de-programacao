
#O Programa de Bonificações por Produtividade (PBP) oferece bonificações de acordo com a produtividade mensal de um 
# funcionário, seguindo as regras abaixo:
# Produtividade abaixo de 50 unidades: não há bonificação;
# Produtividade entre 50 e 100 unidades: bonificação de R$ 100,00;
# Produtividade acima de 100 unidades: bonificação de R$ 200,00.

# Solicite a produtividade mensal do funcionário;
# Verifique se o funcionário tem direito a bonificação, de acordo com as regras do PBP;
# Exiba a bonificação a que o funcionário tem direito.
# Atenção: desenvolva a atividade na célula de código abaixo.

produtividade = int(input("Insira a sua produtividade do mês: "))

if produtividade < 50:
    print("Você não entrou para o Programa de Bonificação por Produtividade.")
elif produtividade >= 50 and produtividade <= 100:
    bonificacao = 100.00 #não precisa disso
    print(f"Você receveu uma bonificação de R$ {bonificacao}")
else:
    bonificacao = 200.00 #não precisa disso
    print(f"Você recebeu uma bonificação de R$ {bonificacao}")
