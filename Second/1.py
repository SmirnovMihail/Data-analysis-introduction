# import numpy as np

def solution1(arg):
    res = [letter*4 for letter in arg]
    return (res)

def solution2(arg):
    return [letter*(i+1) for i, letter in enumerate(arg)]

def solution3(arg):
    return [a for a in arg if a%3 == 0 or a%5 ==0]

def solution4(arg):
    return [x for a in arg for x in a]

def solution5(arg):
    return [(x, y, z) for x in range(arg+1) for y in range(arg+1) for z in range(arg+1) \
    if (x**2 + y**2)==(z**2) and x*y*z!=0 and x < y and y < z]
    
def solution6(arg):
    return [list(x + y for x in arg[1]) for y in arg[0]]

def solution7(arg):
    return [list(x[i] for x in arg) for i in range(len(arg[0]))]

def solution8(arg):
    return [list(map(int , x.split())) for x in arg]

def solution9(arg):
    return {chr(i + ord('a')): i**2 for i in arg}

def solution10(arg):
    return (set(x.lower().title() for x in arg if len(x)>3))

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

# # arg = ([0, 1, 2], [0, 1, 2, 3, 4])
# arg = ['Alice', 'vova', 'ANTON', 'Bob', 'kAMILA', 'CJ', 'ALICE', 'Nastya']
# res = solution10(arg)
# print(res)