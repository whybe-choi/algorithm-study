def solution(lines):
    lengths = [set(range(line[0], line[1])) for line in lines]
    answer = len(lengths[0] & lengths[1] | lengths[0] & lengths[2] | lengths[1] & lengths[2])
    return answer