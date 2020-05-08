n, k = map(int, input().split())
k -= 2 
n -= k
a = []
for i in range(0, n):
    a.append(i %2 + 1)
for i in range(0, k):
    a.append(i + 3)
print(*a, end = ' ')
