valorN = int(input())
dados = input().split()

vetorX = [0] * valorN
menorValor = 0
posicaoMenorValor = 0

for i in range(valorN):
    vetorX[i] = int(dados[i])

for i in range(1, valorN):
    # Compara o elemento atual com o menor encontrado até agora [8, 9].
    if vetorX[i] < vetorX[posicaoMenorValor]:
        posicaoMenorValor = i
        menorValor = vetorX[i]

print(f"Menor valor: {menorValor}")
print(f"Posicao: {posicaoMenorValor}")

