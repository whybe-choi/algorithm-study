def solution(food):
    answer = '0'
    for i in range(len(food)-1, 0, -1):
        answer = f'{i}' * (food[i] // 2) + answer + f'{i}' * (food[i] // 2)
    return answer