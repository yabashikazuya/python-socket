#!/usr/bin/env python
"""
永続的にmessageを送り続けるけながら
別の処理を行いたい
見かけ上の並列処理(らしい)
https://qiita.com/everylittle/items/57da997d9e0507050085#asynciosleep
"""
import asyncio
import websockets
import time

async def echo(websocket, path):
    # async for message in websocket:
    await websocket.send('message')

async def wbsocket():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()
async def sub():
    for i in range(1000000):
        print(i)
        # tome.sleep()ではソケット通信が行えない
        # time.sleep(1)
        await asyncio.sleep(1)

async def main():
    # Task preparation
    socket = asyncio.create_task(wbsocket())
    subprocess = asyncio.create_task(sub())
    await asyncio.gather(socket, subprocess)

asyncio.run(main())