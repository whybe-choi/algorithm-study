def solution(array, n):
    arr = [abs(n - i) for i in sorted(array)]
    for j in range(len(arr)):
        if arr[j] == min(arr):
            return sorted(array)[j]