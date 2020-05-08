from math import ceil

# def print_by_cols(v, cols):
#     for i in range(0, len(v), cols):
#         print(*v[i:i+cols], sep='\t')

def reorder_list(p, cols):
    v = p.copy()
    rest = len(v) %cols
    if rest != 0:
        full = list(range(rest))
        half = list(range(cols - rest))
    else:
        full = list(range(cols))
        half = list()
    d = {}
    v.reverse()
    l = ceil(len(v) /cols)
    for j in full:
        for i in range(l):
            d[j+cols*i] = v.pop()
    half = [x + rest for x in half]
    for j in half:
        for i in range(l - 1):
            d[j+cols*i] = v.pop()
    list_keys = list(d.keys())
    list_keys.sort()
    res=[]
    for i in list_keys:
        res.append(d[i])
    return res

# v = list(range(-10, 5))
# cols = 4

# v_new = reorder_list(v, cols)

# print_by_cols(v, cols)
# print()
# print_by_cols(v_new, cols)