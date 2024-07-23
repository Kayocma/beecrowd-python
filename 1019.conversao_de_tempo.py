# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

# Entrada
# O arquivo de entrada contém um valor inteiro N.

# Saída
# Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.


N = int(input()) # Recebe um valor inteiro e armazena na variável N

H = N // 3600 # Calcula as horas
M = (N % 3600) // 60 # Calcula os minutos
S = (N % 3600) % 60 # Calcula os segundos

print("%d:%d:%d" % (H, M, S)) # Exibe o valor de H, M e S na tela