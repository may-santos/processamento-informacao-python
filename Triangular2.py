n = int(input())
is_upper = True
is_lower = True

for i in range(n):
    row = list(map(int, input().split()))
    for j, val in enumerate(row):
        if i > j and val != 0:
            is_upper = False
        if i < j and val != 0:
            is_lower = False
    if not is_upper and not is_lower:
        for _ in range(i+1, n):
            input()
        break

if is_upper and is_lower:
    print("SIM: DIAGONAL")
elif is_upper:
    print("SIM: SUPERIOR")
elif is_lower:
    print("SIM: INFERIOR")
else:
    print("NAO")