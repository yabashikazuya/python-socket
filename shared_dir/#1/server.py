#!/usr/bin/env python
"""
クライアントからメッセージを受信し、同じメッセージを返す単純なサーバ
"""
import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())

if __name__ == '__main__':
    asyncio.run(main())