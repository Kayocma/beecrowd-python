A, B, C = map(int, input().split()) # Recebe os valores de A, B e C e os converte para int

maiorAB = (A + B + abs(A - B)) // 2 # Calcula o maior valor entre A e B

maior = (maiorAB + C + abs(maiorAB - C)) // 2 # Calcula o maior valor entre o maior valor entre A e B e C

print("%d eh o maior" % maior) # Exibe o maior valor entre A, B e C