from itertools import combinations
import sys

while True:
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    k = nums[0]
    
    if k == 0:
        break
        
    combs = combinations(nums[1:], 6)
    for comb in list(combs):
        print(' '.join(map(str, sorted(list(comb)))))
    print()
    