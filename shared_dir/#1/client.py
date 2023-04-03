#!/usr/bin/env python

# 非同期処理を行うための標準ライブラリ
# import asyncio
# from websockets.sync.client import connect

# def hello():
#     # connect()関数を呼び出してwebsocketを確立、websocket変数にwebsocketオブジェクトを代入
#     with connect("ws://localhost:8765") as websocket:
#         """
#         ブロック内の処理が終了したらWebSocket接続を自動的に閉じる
#         """
#         websocket.send("Hello world!")
#         message = websocket.recv()
#         print(f"Received: {message}")

import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("aaa")
        print(await websocket.recv())




if __name__ == '__main__':
    asyncio.run(hello())
