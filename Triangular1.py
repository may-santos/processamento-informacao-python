n = int(input())
is_upper = True
for i in range(n):
    row = list(map(int, input().split()))
    for j, val in enumerate(row):
        if i > j and val != 0:
            is_upper = False
            break
    if not is_upper:
        for _ in range(i+1, n):
            input()
        break

print("SIM" if is_upper else "NAO")