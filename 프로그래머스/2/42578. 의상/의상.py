def solution(clothes):
    answer = 1
    fashion = dict()
    for clothe, category in clothes:
        if category not in fashion.keys():
            fashion[category] = [clothe]
        else:
            fashion[category].append(clothe)

    for _, value in fashion.items():
        answer *= len(value) + 1
    return answer - 1