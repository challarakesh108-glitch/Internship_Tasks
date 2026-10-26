#Q20

from collections import deque

def can_stack(cubes):
    dq = deque(cubes)
    last = float('inf')  
    while dq:
        
        if dq[0] >= dq[-1]:
            current = dq.popleft()
        else:
            current = dq.pop()
        
        
        if current > last:
            return "No"
        last = current
    return "Yes"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        cubes = list(map(int, input().split()))
        print(can_stack(cubes))
