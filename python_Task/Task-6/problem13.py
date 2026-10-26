#Q13

if __name__ == '__main__':
    n = int(input())  
    english = set(map(int, input().split()))
    
    m = int(input())  
    french = set(map(int, input().split()))
    
    
    total = english.union(french)
    
    print(len(total))
