import copy

class FragileDict:

    def __init__(self, d={}, lock=True):
        self._data = copy.deepcopy(d)
        self._lock = lock
        # print('init')


    def __contains__(self, item):

        if self._lock:
            return item in self._data
        else:
            return item in self.copy_data


    def __getitem__(self, item):

        if self._lock and item in self._data:
            c = copy.deepcopy(self._data[item])
            # print(c)
            return c 
        elif not self._lock and item in self.copy_data:
            return self.copy_data[item]
        else:
            raise KeyError(item)


    def __enter__(self):

        self._lock = False
        self.copy_data = copy.deepcopy(self._data)
        return self._data


    def __exit__(self, exc_type, exc_val, exc_tb):

        self._lock = True
        if exc_type is not None:
            delattr(self, 'copy_data')
            print('Exception has been suppressed.')
            return True
        self._data = copy.deepcopy(self.copy_data)
        delattr(self, 'copy_data')


    def __setitem__(self, key, val):

        if self._lock:
            raise RuntimeError("Protected state")
        self.copy_data[key] = val


# d = FragileDict({'key': []})

# with d:
#     a = d['key']
#     d['key'].append(10)
#     a.append(10)

# a.append(10)
# print(a == [10, 10, 10] and d['key'] == [10, 10])

# d = FragileDict({'key': 5})

# d = FragileDict({'key': 5})

# with d:
#     d['key'] = 6
#     print(d['key'])
#     d['ord'] = 7
#     print('ord' in d and d['ord'] == 7)
#     raise Exception()

# print(d['key'])
# print('ord' not in d)
