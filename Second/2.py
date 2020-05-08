import re
import operator as op
from functools import reduce

def solution1(arg):
    return list(map(lambda x: int(re.sub('[.,-]', '', x.strip())[::-1]), arg))

def solution2(arg):
    return list(map(lambda p: p[0]*p[1], list(arg)))

def solution3(arg):
    return list(filter(lambda x: x%6 == 0 or x%6 == 2 or x%6 == 5, arg))

def solution4(arg):
    return list(filter(lambda x: bool(x) == True, arg))

def solution5(arg):
    # print
    return list(map(lambda x: x.update({"square": x['width'] * x["length"]}), arg))
    # (map(op.setitem(arg[i], "square", arg[i]["width"]*arg[i]["length"] ), arg) for i in range[len(arg)])
    # print(arg)

def solution6(arg):
    return list(map(lambda x: dict(zip(list(x.keys()) + ['square'],
                list(x.values()) + [x['length'] * x['width']])), arg))

def solution7(arg):
    return reduce(lambda x, y: x.intersection(y), arg)

def solution8(arg):
    return reduce(lambda x, y: op.setitem(x, y, x[y]+ 1) or x, [dict.fromkeys(arg, 0)] + arg)

def solution9(arg):
    return list(map(lambda st: st['name'], list(filter(lambda x: x['gpa'] > 4.5, arg))))

def solution10(arg):
    return list(filter(lambda x: not reduce(lambda c, b: c + b, list(map(lambda t: -1 * int(t[1]) if t[0] % 2 == 0 else int(t[1]),
                                                                         list(enumerate(list(x)))))), arg))


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}
# arg = [1, 2, 1, 1, 3, 2, 3, 2, 4, 2, 4]
# rooms = [
#     {"name": "комната1", "width": 2, "length": 4},
#     {"name": "комната2", "width": 2.5, "length": 5.6},
#     {"name": "кухня", "width": 3.5, "length": 4},
#     {"name": "туалет", "width": 1.5, "length": 1.5},
# ]
# op.setitem(rooms[0], "square", rooms[0]["width"]*rooms[0]["length"])
# print(rooms)
# arg = rooms
# res = solution8(arg)
# print(res)