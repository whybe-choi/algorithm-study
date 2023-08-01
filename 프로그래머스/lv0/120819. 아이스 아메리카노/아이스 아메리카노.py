def solution(money):
    cup = money // 5500
    changes = money % 5500
    answer = [cup, changes]
    return answer