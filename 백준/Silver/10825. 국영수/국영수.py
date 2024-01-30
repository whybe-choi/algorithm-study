import sys

n = int(sys.stdin.readline().rstrip())
students = []

for _ in range(n):
    student, korean, english, math = sys.stdin.readline().rstrip().split()
    students.append([student, int(korean), int(english), int(math)])
    
for student, _, _, _ in sorted(students, key=lambda x : (-x[1], x[2], -x[3], x[0])):
    print(student)
    