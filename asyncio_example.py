import asyncio


@asyncio.coroutine #makes generator out of function
def print_nums():
    num = 1
    while True:
        print(num)
        num +=1
        yield from asyncio.sleep(1) #passes control to event loop

@asyncio.coroutine
def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} seconds have passed".format(count))
        count += 1
        yield from asyncio.sleep(1)

@asyncio.coroutine
def main():
    task1 = asyncio.ensure_future(print_nums()) #inserts into event loop
    task2 = asyncio.ensure_future(print_time()) #parens are needed since print_time() is a gen
    
    #gather collects results ans is also a generator
    yield from asyncio.gather(task1, task2)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
