n=int(input())
l = (int(i) for i in input().split())
d = {}
lst = []
for x in l:
    lst.append((x //10 + x %10,x))
lst.sort()
res=[]
for i in lst:
    print(i[1], end=' ')
print()