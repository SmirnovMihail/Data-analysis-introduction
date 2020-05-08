import sys


def request(l, r):
    rest = (r - l)/10
    x = l + rest
    for i in range(1, 11):
        print('?', int(l + i*rest))
    print('+')

def info():
    a = []
    for i in range(10):
        a.append(int(input()))
    return a

def check(a):
    for i in a:
        if i == 1:
            return a.index(i)
    return len(a)

def main(l ,r):
    rest = int((r - l)/10)
    if rest == 0:
        return l
    else:
        request(l, r)
        sys.stdout.flush()
        a = info()
        # print(a)
        num = check(a)
        # print(num)
        if num == 10:
            return r
        else:
            return main(l + rest*num, l + rest*(num + 1))

res = main(0, 100000)
print('!', res)