# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

# Saída
# Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.


N = int(input()) # Recebe um valor inteiro e armazena na variável N
print(N) # Exibe o valor de N na tela
print("%d nota(s) de R$ 100,00" % (N // 100)) # Exibe o valor de N dividido por 100
N = N % 100 # N recebe o resto da divisão de N por 100
print("%d nota(s) de R$ 50,00" % (N // 50)) # Exibe o valor de N dividido por 50
N = N % 50 # N recebe o resto da divisão de N por 50
print("%d nota(s) de R$ 20,00" % (N // 20)) # Exibe o valor de N dividido por 20
N = N % 20 # N recebe o resto da divisão de N por 20
print("%d nota(s) de R$ 10,00" % (N // 10)) # Exibe o valor de N dividido por 10
N = N % 10 # N recebe o resto da divisão de N por 10
print("%d nota(s) de R$ 5,00" % (N // 5)) # Exibe o valor de N dividido por 5
N = N % 5 # N recebe o resto da divisão de N por 5
print("%d nota(s) de R$ 2,00" % (N // 2)) # Exibe o valor de N dividido por 2
N = N % 2 # N recebe o resto da divisão de N por 2
print("%d nota(s) de R$ 1,00" % (N // 1)) # Exibe o valor de N dividido por 1
N = N % 1 # N recebe o resto da divisão de N por 1