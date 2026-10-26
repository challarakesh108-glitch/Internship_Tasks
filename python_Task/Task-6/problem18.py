#Q18

if __name__ == '__main__':
    A = set(input().split())
    n = int(input())
    result = True
    for _ in range(n):
        other = set(input().split())
        if not A.issuperset(other) or A == other:
            result = False
            break
    print(result)
