#!/usr/bin/env python
"""
永続的にmessageを送り続けるサーバ
"""
import asyncio
import websockets

async def echo(websocket, path):
    # async for message in websocket:
    await websocket.send('message')

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()

asyncio.run(main())