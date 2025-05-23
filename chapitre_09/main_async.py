import asyncio
import time


async def add(a,b):
    await asyncio.sleep(1)
    return a+b

# Async
async def main():
    start = time.time()
    # print('Hello ...')
    # await asyncio.sleep(1)
    # print('... World!')
    # c = await add(1,2)
    # print(c)
    # c1 = await add(4,8)
    # print(c1)

    coroutines = [add(1,2),add(4,8)]
    r = await asyncio.gather(*coroutines)
    print(r)
    end = time.time()

    print(f"{end-start:.3}s")

if __name__ == '__main__':
    asyncio.run(main())


# Sync

# def main():
#     print('Hello ...')
#     time.sleep(1)
#     print('... World!')

# if __name__ == '__main__':
#     main()