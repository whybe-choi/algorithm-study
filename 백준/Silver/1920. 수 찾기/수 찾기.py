import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1

        if arr[mid] > target:
            right = mid - 1
        else: 
            left = mid + 1
    return 0

sorted_a = sorted(a)

for i in range(len(b)):
    print(binary_search(sorted_a, b[i]))