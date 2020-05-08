n = int(input())
s = set()
j = 0
l = list(int(i) for i in input().split())
for elem in l:
    if elem not in s:
        s.add(elem)
        print(elem, end =' ')
    else:
        j += 1
print()
print(j)
