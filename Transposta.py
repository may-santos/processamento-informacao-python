n = int(input())
m = int(input())

matriz = []
for _ in range (n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

for j in range(m):
    trans_row = [str(matriz[i][j]) for i in range(n)]
    print(' '.join(trans_row))