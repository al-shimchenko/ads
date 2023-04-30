def longest_increasing_subsequence(arr):
    tails = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] < tails[0]:
            tails[0] = arr[i]
        elif arr[i] > tails[-1]:
            tails.append(arr[i])
        else:
            left, right = 0, len(tails) - 1
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < arr[i]:
                    left = mid + 1
                else:
                    right = mid
            tails[right] = arr[i]
    return tails

N = [-10, 5, 7, 9, -3, 2, 4, 6]
print(longest_increasing_subsequence(N))
