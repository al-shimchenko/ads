coins = [10, 5, 2, 1]
amounts = [5, 3, 4, 6]
change = 28
result = []

for i in range(len(coins)):
    if coins[i] <= change and amounts[i] > 0:
        num = min(change // coins[i], amounts[i])
        result.extend([coins[i]] * num)
        change -= coins[i] * num

if change == 0:
    print("Сдача состоит из следующих монет:", result)
else:
    print("Невозможно дать сдачу заданными монетами")
