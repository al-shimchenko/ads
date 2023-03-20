def knapsack(exhibits, m, k):
    exhibits.sort(key=lambda x: x[1] / x[0], reverse=True)

    weight = 0
    value = 0

    chosen = []

    for i in range(m):
        for j in range(len(exhibits)):
            if j not in chosen and exhibits[j][0] <= k - weight:
                chosen.append(j)
                weight += exhibits[j][0]
                value += exhibits[j][1]
        weight = 0
    return value, chosen


exhibits = [(2, 2000000), (3, 900000), (4, 400000), (5, 100000)]
m = 2
k = 5

ans = []
a, b = knapsack(exhibits, m, k)
for c in b:
    ans.append(exhibits[c])

print(f'Максимальная стоимость экспонатов равна {a}, были взяты экспонаты {ans}')
