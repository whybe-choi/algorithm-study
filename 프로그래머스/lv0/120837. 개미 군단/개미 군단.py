def solution(hp):
    general = hp // 5
    solder = (hp % 5) // 3
    worker = ((hp % 5) % 3) // 1
    answer = general + solder + worker
    return answer