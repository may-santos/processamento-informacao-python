saidas = []

while True:
    valor = int(input())
    if valor == 0:
        break

    vetor = list(map(int, input().split()))
    for i in range(valor):
        if vetor[i] % 2 == 0:
            vetor[i] = 0
        else:
            vetor[i] = 1

    saidas.append(" ".join(map(str, vetor)))

if saidas:
    print("\n".join(saidas))