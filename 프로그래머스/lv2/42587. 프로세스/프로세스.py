from collections import deque

def solution(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    count = 0
    
    priorities.sort(reverse=True)
    
    while True:
        value, _ = queue[0];
        if value < priorities[count]:
            queue.rotate(-1)
        else:
            _, index = queue.popleft()
            count += 1
            if location == index:
                break
            
    return count