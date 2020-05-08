from collections import defaultdict

def smartdict_nan(key):
    return 10 * key

N = 10

smartdict = {}
for key in range(N):
    val = defaultdict(lambda: smartdict_nan(key))
    # print(id(val), val)
    smartdict[key] = val
    smartdict[key]['key_unknown']

print(smartdict[5]['key_unknown'])
print(smartdict[2]['key_unknown'])
print(smartdict[7]['key_unknown'])

#Так как defaultdict является подклассом dict для создания пары 
#ключ значение ему не хватает только значения, нужен ключ, поэтому добавление строки smartdict[key]['key_unknown']решает нашу проблему