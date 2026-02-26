valor = int(input())
vetor = list(map(int, input().split()))

for i in range(valor):
    if vetor[i] % 2 == 0:
        vetor[i] = 0
    else:
        vetor[i] = 1

print(*vetor)