"""Triângulo de Floyd"""


n = int(input('Insira um número: '))    # Número de linhas no triângulo
num = 1    # Contador inicial

for i in range(1, n + 1):   # Loop para o número de linhas
    for j in range(1, i + 1):   # Loop para os números em uma linha
        print(num, end=' ')
        num += 1
    print()
