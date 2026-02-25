n, m = map(int, input().split())

min_sum = None
for _ in range(n):
    row = list(map(int, input().split()))
    s = sum(row)
    if min_sum is None or s < min_sum:
        min_sum = s

print(min_sum)
