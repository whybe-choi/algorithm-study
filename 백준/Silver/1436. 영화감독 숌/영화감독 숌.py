import sys

n = int(sys.stdin.readline().rstrip())
nums = []
num = 0

while len(nums) != n:
    
    if '666' in str(num):
        nums.append(num)
    
    num += 1
        
print(nums[n-1])
        

    
