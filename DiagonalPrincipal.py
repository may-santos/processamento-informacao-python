operacao = input()
quantidade_numeros = int(input())
numeros = [[]]

for i in range(quantidade_numeros):
    linha = input().split()
    numeros.append(linha)


if operacao == "S":
    soma = 0
    for i in range(1, quantidade_numeros + 1):
        soma += int(numeros[i][i - 1])
    print(f"{soma:.1f}")
else:
    media = 0
    for i in range(1, quantidade_numeros + 1):
        media += int(numeros[i][i - 1])
    media /= quantidade_numeros
    print(f"{media:.1f}")


