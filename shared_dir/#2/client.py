#!/usr/bin/env python
"""
永続的にwebsocketを受け取り続けるプログラム
"""
import asyncio
import websockets

async def my_coroutine():
    while True:
        try:
            async with websockets.connect('ws://localhost:8765') as websocket:
                while True:
                    message = await websocket.recv()
                    print(f"Received: {message}")
        except:
            pass
        await asyncio.sleep(3)

asyncio.run(my_coroutine())
