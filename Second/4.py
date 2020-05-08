import time
import functools

def counter(func):
    @functools.wraps(func)
    def wrapper(*args, **argv):
        if not hasattr(wrapper, 'start_flag'):
            setattr(wrapper, 'start_flag', 0) 
        if wrapper.start_flag == 0:
            setattr(wrapper, 'ncalls', 0)
            setattr(wrapper, 'rdepth', 0)
            setattr(wrapper, 'max_rdepth', 0)
            wrapper.start_flag = 1
        wrapper.ncalls += 1
        wrapper.rdepth += 1
        res = func(*args, **argv)
        if wrapper.rdepth > wrapper.max_rdepth:
            wrapper.max_rdepth = wrapper.rdepth
        wrapper.rdepth -= 1
        if wrapper.rdepth == 0:
            wrapper.start_flag = 0
            wrapper.rdepth = wrapper.max_rdepth
        return res
    return wrapper

# @counter
# def func2(n, steps):
#     if steps == 0:
#         return

#     func2(n + 1, steps - 1)
#     func2(n - 1, steps - 1)

# if __name__ == "__main__":
#     func2(0, 5)
#     print(func2.ncalls, func2.rdepth)

#     func2(0, 3)
#     print(func2.ncalls, func2.rdepth)