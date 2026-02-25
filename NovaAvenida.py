n, m = map(int, input().split())

col_sums = [0] * m
for _ in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        col_sums[j] += row[j]

resultado = min(col_sums)
print(resultado)