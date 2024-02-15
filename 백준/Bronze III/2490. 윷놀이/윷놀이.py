import sys

grade = {1:'A', 2:'B', 3:'C', 4:'D', 0:'E'}

for _ in range(3):
    yut = list(sys.stdin.readline().rstrip().split())
    count = yut.count('0')
    print(grade[count])