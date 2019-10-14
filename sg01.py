def coroutine(func): # instead of f.send(None) or f.__next__() to init generator
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

class BlaBlaException(Exception):
    pass



#@coroutine
def sg_coro():
    while True:
        try:
            message = yield
        except BlaBlaException:
            print('Exc handler in subgen coro!')
        except StopIteration:
            break
        else:
            print('..............', message)
    return 'Subgen all done!'

@coroutine
def delegator_coro(g):
    result = yield from g
    print(result)
