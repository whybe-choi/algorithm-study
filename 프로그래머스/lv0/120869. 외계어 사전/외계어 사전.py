def solution(spell, dic):
    answer = 2
    for string in dic:
        if set(spell) == set(string):
            answer = 1
    return answer