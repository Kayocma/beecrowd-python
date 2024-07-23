NUMBER = int(input()) # Recebe o número do funcionário
HOURS = int(input()) # Recebe o número de horas trabalhadas
SALARY = float(input()) # Recebe o valor da hora trabalhada

SALARY = HOURS * SALARY # Calcula o salário do funcionário com base nas horas trabalhadas e no valor da hora trabalhada

print("NUMBER = %d" % NUMBER) # Exibe o número do funcionário
print("SALARY = U$ %.2f" % SALARY) # Exibe o salário do funcionário com duas casas decimais