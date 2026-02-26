import sys

def minimo_moedas(M, coins):
    INF = M + 1
    dp = [INF] * (M + 1)
    dp[0] = 0
    for c in coins:
        for v in range(c, M + 1):
            if dp[v - c] + 1 < dp[v]:
                dp[v] = dp[v - c] + 1
    return dp[M] if dp[M] != INF else None


def main():
    while True:
        try:
            linha = input().strip()
        except EOFError:
            break
        if not linha:
            continue
        M, N = map(int, linha.split())
        if M == 0:
            break
        coins = list(map(int, input().split()))
        res = minimo_moedas(M, coins)
        if res is None:
            print("impossivel")
        else:
            print(res)
        print()


if __name__ == "__main__":
    main()
