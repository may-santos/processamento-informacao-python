N, K = map(int, input().split())

matriz = []
for _ in range(N):
    linha = list(map(int, input().split()))
    matriz.append(linha)

soma = 0
for i in range(N):
    soma += matriz[i][K]

print(soma)
