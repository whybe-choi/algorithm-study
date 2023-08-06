def solution(numbers, k):
    while k * 2 > len(numbers):
        numbers += numbers
    answer = numbers[2 * (k-1)]
    return answer