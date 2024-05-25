from collections import Counter

def solution(topping):
    answer = 0
    # 전체 토핑의 종류를 센다.
    right_counter = Counter(topping)
    left_counter = Counter()
    
    for i in range(len(topping) - 1):
        # 현재 토핑을 오른쪽에서 왼쪽으로 이동
        topping_type = topping[i]
        left_counter[topping_type] += 1
        right_counter[topping_type] -= 1
        
        # 오른쪽 카운터에서 토핑 종류의 개수가 0이 되면 제거
        if right_counter[topping_type] == 0:
            del right_counter[topping_type]

        # 두 부분의 토핑 종류의 개수를 비교
        if len(left_counter) == len(right_counter):
            answer += 1

    return answer