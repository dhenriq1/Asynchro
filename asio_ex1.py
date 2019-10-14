import asyncio


#makes generator out of function
async def print_nums():
    num = 1
    while True:
        print(num)
        num +=1
        await asyncio.sleep(1) #passes control to event loop


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} seconds have passed".format(count))
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_nums()) #inserts into event loop
    task2 = asyncio.create_task(print_time()) #parens are needed since print_time() is a gen
    
    #gather collects results ans is also a generator
    await asyncio.gather(task1, task2)

if __name__ == '__main__':
#    loop = asyncio.get_event_loop()
#    loop.run_until_complete(main())
#    loop.close()
    asyncio.run(main())
