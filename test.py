import asyncio


async def greet_every_two_seconds():
     while True:
        print('Hello World')
        await asyncio.sleep(2)

asyncio.run(greet_every_two_seconds())