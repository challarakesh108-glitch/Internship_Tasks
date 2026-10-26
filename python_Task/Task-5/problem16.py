#Q16

from collections import Counter

n = int(input())
shoe_sizes = list(map(int, input().split()))
x = int(input())

inventory = Counter(shoe_sizes)
earnings = 0

for _ in range(x):
    size, price = map(int, input().split())
    if inventory[size] > 0:
        earnings += price
        inventory[size] -= 1

print(earnings)
