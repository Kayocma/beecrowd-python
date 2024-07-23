PECA1 = input().split() # Recebe o código, a quantidade e o valor unitário da primeira peça
PECA2 = input().split() # Recebe o código, a quantidade e o valor unitário da segunda peça

CODIGO1, NUMERO1, VALOR1 = PECA1 # Atribui o código, a quantidade e o valor unitário da primeira peça a variáveis
CODIGO2, NUMERO2, VALOR2 = PECA2 # Atribui o código, a quantidade e o valor unitário da segunda peça a variáveis

TOTAL = (int(NUMERO1) * float(VALOR1)) + (int(NUMERO2) * float(VALOR2)) # Calcula o total a ser pago

print("VALOR A PAGAR: R$ %.2f" % TOTAL) # Exibe o total a ser pago com duas casas decimais