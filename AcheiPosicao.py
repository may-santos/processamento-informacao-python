n = int(input())
linha = input().split()

v = []

for i in range(n):
    v.append(int(linha[i]))

contVerifica = int(input())
verificacao = []

for _ in range(contVerifica):
    valor = int(input())
    if valor in v:
        verificacao.append(str(v.index(valor)))
    else:
        verificacao.append("-1")

for i in range(len(verificacao)):
    print(verificacao[i])
