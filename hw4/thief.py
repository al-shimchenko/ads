def thief(N, M, K, W, P):
    dp = [[0 for _ in range(M * K + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M * K + 1):
            if W[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W[i - 1]] + P[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    i = N
    j = M * K
    stolen = []

    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            stolen.append(i - 1)
            j -= W[i - 1]
        i -= 1

    return dp[N][M * K], stolen


N = 5
M = 2
K = 10
W = [3, 2, 5, 4, 7]
P = [1000, 800, 5000, 3000, 4000]

result = thief(N, M, K, W, P)
print("Максимальная цена:", result[0])
print("Украденные экспонаты:", result[1][::-1])
