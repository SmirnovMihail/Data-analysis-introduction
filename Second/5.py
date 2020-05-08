def chain_loop(args):
    check = {}
    list_a = args
    list_a = list(filter(lambda x: bool(x) == True, args))
    length = len(list_a)
    list_a = list(map(iter, list_a))
    for i in range(length):
        check[i] = 0
    j = 0
    k = 0
    while j >= 0:
        try:
            for i in range(k, length):
                if check[i] == 0:
                    yield next(list_a[i])

            k = 0

        except (StopIteration):
            k = i + 1
            check[i] = 1
            continue

        flag = 1
        # print(check)
        for i in range(length):
            if check[i] == 0:
                flag = 0
        if flag == 1:
            j = -1
        


# a = (i for i in range(10))
# b = a

# print(list(chain_loop([a, b])))
# b = []
# c = []
# f = ''
# a = range(3)
# b = 'python'
# c = [None, None, None]
# d = {10, 20, 30, 40, 50}
# print(list(chain_loop([a, b, c, d])))
# it = iter(a)
# print(next(it))
# print(next(it))
# for i in a:
#     print(a,i)""
# chain_loop([a, b, c])
# a = 'python'
# b = [1] * 5
# c = [None, None, None]

# print(list(chain_loop([a, b, c])))
