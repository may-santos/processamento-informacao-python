operacao = input()
quantidade = int(input())

numeros = [[]]
for i in range(quantidade):
    linha = input().split()
    numeros.append(linha)

if operacao == "S":
    soma = 0
    for i in range(1, quantidade + 1):
        for j in range(1, i):
            soma += int(numeros[i][j - 1])
    print(f"{soma:.1f}")
else:
    media = 0
    for i in range(1, quantidade + 1):
        for j in range(1, i):
            media += int(numeros[i][j - 1])
    media /= (quantidade * (quantidade - 1) / 2)
    print(f"{media:.1f}")