#import matplotlib.pyplot as plt

#задание 1
def game_result(game):
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] != ' ':
            return f"{game[i][0]} - победитель"
        if game[0][i] == game[1][i] == game[2][i] != ' ':
            return f"{game[0][i]} - победитель"
    if game[0][0] == game[1][1] == game[2][2] != ' ':
        return f"{game[0][0]} - победитель"
    if game[0][2] == game[1][1] == game[2][0] != ' ':
        return f"{game[0][2]} - победитель"
    return 'Ничья'

#задание 2
def bin_search(matrix, x):

    rows = len(matrix)
    cols = len(matrix[0])
    left = 0
    right = rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        mid_el = matrix[mid // cols][mid % cols]
        if mid_el == x:
            return (mid // cols) + 1, (mid % cols) + 1
        else:
            if x < mid_el:
                right = mid - 1
            else:
                left = mid + 1

    return 'Искомый элемент не содержится в матрице'

# задание 3
def queen(n):
    if n == 0:
        return [[]]
    smaller_solutions = queen(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(8)
            for solution in smaller_solutions
            if all(not is_under_attack(n, i + 1, x, y) for x, y in solution)]

def is_under_attack(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2 or x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2

# задание 4
def count_ways(n):

  if n == 0:
    return 1
  elif n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
      return 3

  return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3) + count_ways(n - 4)

#задание 6
def exp_filter(x, a):
  y = [x[0]]
  for i in range(1, len(x)):
    y.append(a * x[i] + (1 - a) * y[i-1])
  return y

# задание 7
def find_min(nums):
    num_set = set(nums)
    i = 1
    while True:
        if i not in num_set:
            return i
        i += 1

game = [['X', 'O', 'X'],
         ['O', 'X', 'O'],
         ['O', 'X', 'X']]

matrix = [[1, 5, 7],
          [9, 11, 17],
          [22, 23, 40]]

x = [10, 12, 15, 13, 11, 9, 8, 7, 6, 5]
a = 0.5

nums = [3, 4, -1, 2, 1, 6, 7]
result = find_min(nums)

# print(game_result(game))
# print(bin_search(matrix, 17))
# for answer in queen(8):
#    print(answer)
# print(count_ways(5))
# print(exp_filter(x, a))
print(f"Наименьшее пропущенное целое число: {result}")

# y=exp_filter(x, a)
# plt.plot(x, label="signal")
# plt.plot(y, label="filter")
# plt.legend()
# plt.show()




