linha1 = input().split()
linha2 = input().split()
linha3 = input().split()

quantidade_figurinhas = int(linha1[0])
quantidade_carimbadas = int(linha1[1])
quantidade_compradas = int(linha1[2])

carimbadas = set(map(int, linha2))
compradas = set(map(int, linha3))

faltam = len(carimbadas - compradas)
print(faltam)
