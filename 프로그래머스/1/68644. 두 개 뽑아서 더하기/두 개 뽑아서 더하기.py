from itertools import combinations

def solution(numbers):
    s = set()
    combs = list(combinations(numbers, 2))
    for comb in combs:
        s.add(sum(comb))
    return sorted(list(s))