#Q14

if __name__ == '__main__':
    n = int(input())  
    english = set(map(int, input().split()))
    
    m = int(input())  
    french = set(map(int, input().split()))
    
    
    both = english.intersection(french)
    
    print(len(both))
