"""
func1とfunc2を並列処理させる
"""
import asyncio

async def func1():
    print('func1() started')
    await asyncio.sleep(10)
    print('func1() finished')

async def func2():
    print('func2() started')
    await asyncio.sleep(1)
    print('func2() finished')

async def main():
    # task1,task2をスタンバイさせる
    task1 = asyncio.create_task(func1())
    task2 = asyncio.create_task(func2())
    await asyncio.gather(task1, task2)

asyncio.run(main())
