def Matrix(p):
    n = len(p) - 1
    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    s = [[None for _ in range(n + 1)] for _ in range(n)]

    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m[1][n], s

def brackets(s,i,j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        brackets(s, i, s[i][j])
        brackets(s, s[i][j] + 1, j)
        print(")", end="")

p = [10, 20, 30, 40, 30]
n = len(p) - 1
m,s= Matrix(p)
print(f'Минимальное количество скалярных операций - {m}')
brackets(s, 1, n)


