NOME = str(input()) # Recebe o nome do funcionário
SALARIO = float(input()) # Recebe o salário fixo do funcionário
VENDAS = float(input()) # Recebe o valor total de vendas do funcionário 

TOTAL = SALARIO + (VENDAS * 0.15) # Calcula o salário total do funcionário com base no salário fixo e no valor total de vendas

print("TOTAL = R$ %.2f" % TOTAL) # Exibe o salário total do funcionário com duas casas decimais