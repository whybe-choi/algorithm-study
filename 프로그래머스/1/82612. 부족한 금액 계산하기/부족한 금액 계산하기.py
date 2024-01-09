def solution(price, money, count):
    total = sum([price * i for i in range(1, count+1)])
    answer = total - money if total > money else 0

    return answer