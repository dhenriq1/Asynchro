def coroutine(func): # instead of f.send(None) or f.__next__() to init generator
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

def subgen():
    x = 'yield returns this'
    message = yield x
    print('Message received: ', message)

class BlaBlaException(Exception):
    pass

@coroutine
def average():
    count=0
    sum=0
    average=None

    while True:

        try:
            x = yield average # returns average with every cycle
        except StopIteration:
            print('Done')
            break
        except BlaBlaException:
            print('Custom exception thrown')
            break
        else:
            count += 1
            sum += x
            average = round(sum / count, 2)
    

@coroutine
def average2():
    count=0
    sum=0
    average=None

    while True:

        try:
            x = yield 
        except StopIteration:
            print('Done')
            break
        else:
            count += 1
            sum += x
            average = round(sum / count, 2)
            
    return average # returns average only after StopIteration

# result can be caught in the calling function as:
#g = average()
#try:
#    g.throw(StopIteration)
#except StopIteration as e:
#    print('Average: ', e.value)

def sg():
    for i in 'brooklyn':
        yield i
def delegator(g):
    for i in g:
        yield i


# init not needed if yield from is used in delegator
@coroutine
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

    while True:
        try:
            data = yield
            g.send(data)
            
        except BlaBlaException as e: #redirects handling of exc to subgen
            g.throw(e)
 
        except StopIteration as e1: # this is to get return from subgen
            g.throw(e1)
            print('Returned from subgen: ', e1.value)
        

    # all of the above + @coroutine decorator for subgen can be replaced by

#    result = yield from g
#    print(result)
        
        
