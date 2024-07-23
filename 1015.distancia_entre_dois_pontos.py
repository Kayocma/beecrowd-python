eixo_x = input().split() # Recebe os valores de x1 e y1
eixo_y = input().split() # Recebe os valores de x2 e y2
x1, y1 = eixo_x # Atribui o valor de x1 a variável x1 e o valor de y1 a variável y1
x2, y2 = eixo_y # Atribui o valor de x2 a variável x2 e o valor de y2

distancia = ((float(x2) - float(x1)) ** 2 + (float(y2) - float(y1)) ** 2) ** 0.5 # Calcula a distância entre os pontos (x1, y1) e (x2, y2)

print("%.4f" % distancia) # Exibe a distância entre os pontos (x1, y1) e (x2, y2) com quatro casas decimais