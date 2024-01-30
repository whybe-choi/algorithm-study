import sys

n = int(sys.stdin.readline().rstrip())
files = {}

for _ in range(n):
    _, extension = sys.stdin.readline().rstrip().split('.')
    if extension in files.keys():
        files[extension] += 1
    else:
        files[extension] = 1
        
for extension, count in sorted(files.items(), key = lambda x : x[0]):
    print(extension, count)