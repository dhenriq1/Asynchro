import asyncio

# Borrowed from http://curio.readthedocs.org/en/latest/tutorial.html.

@asyncio.coroutine
def countdown(number, n):
    while n > 0:
        print('T-minus', n, '({})'.format(number))
        yield from asyncio.sleep(1)
        n -= 1

loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(countdown("A", 5)),
    asyncio.ensure_future(countdown("B", 6))]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
