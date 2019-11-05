#!/usr/bin/env python

import asyncio
import pathlib
import websockets

async def listen_for_message(websocket):

    while True:
        try:
            message = await websocket.recv()
            print("< {}".format(message))
        except websockets.ConnectionClosed as cc:
            print('Connection closed')
        except Exception as e:
            print('Something happened: ' + str(e))    

async def connect_to_server():
    websocket = await websockets.connect('ws://127.0.0.1:6789/')
    hello_message = await websocket.recv()
    print("< {}".format(hello_message))
    return websocket

async def my_app():
    websocket = await connect_to_server()
    print('We have a connection to the server')
    asyncio.ensure_future(listen_for_message(websocket))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(my_app())
    loop.run_forever() 