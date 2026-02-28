N = int(input())
V = list(map(int, input().split()))

maior = V[0]
posicao = 0

for i in range(1, N):
    if V[i] > maior:
        maior = V[i]
        posicao = i

print(f"Maior valor: {maior}")
print(f"Posicao: {posicao}")
