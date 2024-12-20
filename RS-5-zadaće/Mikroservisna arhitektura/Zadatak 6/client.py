import aiohttp
import asyncio


async def fetch_data(port):
    async with aiohttp.ClientSession() as session:
        rezultat = await session.get(f"http://localhost:{port}/pozdrav")
        return await rezultat.json()


async def main():
    # async with aiohttp.ClientSession() as session:
    #     async with session.get("http://localhost:8081/pozdrav") as response:
    #         print(await response.json())
    #     async with session.get("http://localhost:8082/pozdrav") as response:
    #         print(await response.json())

    rezultati = await asyncio.gather(fetch_data(8081), fetch_data(8082))
    print(rezultati)

asyncio.run(main())
