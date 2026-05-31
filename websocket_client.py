import asyncio
import websockets




async def client():
    url = "ws://localhost:8765"
    async with websockets.connect(url) as websocket:
        messages = "Привет, сервер!"
        print(f"Отправка: {messages}")
        await websocket.send(messages)

        for _ in range(5):
            response = await websocket.recv()
            print(f"Ответ от сервера: {response}")


asyncio.run(client())

