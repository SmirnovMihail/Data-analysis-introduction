import time
import functools

def timeout(rps):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **argv):
            t = time.time()
            # if not hasattr(wrapper, 'time'):
            #     setatt
            # r(wrapper, 'time', t)
            res = func(*args, **argv)
            delta = time.time() - t
            if delta < 1/rps:
                time.sleep(1/rps - delta)
            return res
            # # print(wrapper.time)
            # # print(time.time())
            # if not hasattr(wrapper, 'counter'):
            #     setattr(wrapper, 'counter', 0) 
            # if (t - wrapper.time >= 1):
            #     wrapper.time = t
            #     wrapper.counter = 0 

            # if wrapper.counter < rps:
            #     # print('ok')
            #     wrapper.counter +=1
            #     return func(*args, **argv)

            # if (time.timaounter +=1
            # return None
        return wrapper
    return decorator

# import time

# @timeout(rps=5)
# def func():
#     pass

# if __name__ == "__main__":
#     t_start = time.time()
#     for i in range(10):
#         func()
#     t_delta = time.time() - t_start
#     print("{:.2f}".format(t_delta))