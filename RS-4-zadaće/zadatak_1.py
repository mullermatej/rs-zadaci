import asyncio
import aiohttp
import ssl
import time

start_time = time.time()


async def fetch_users(session):
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    async with session.get('https://jsonplaceholder.typicode.com/users', ssl=ssl_context) as response:
        elapsed_time = time.time() - start_time
        print(f"Šaljem zahtjev, proteklo vrijeme od početka: {
              elapsed_time:.2f}")
        return await response.json()


async def main():
    async with aiohttp.ClientSession() as session:
        taskovi = [asyncio.create_task(fetch_users(session)) for i in range(5)]
        rezultati = await asyncio.gather(*taskovi)
        imena = list(map(lambda x: [user["name"] for user in x], rezultati))
        emailovi = list(map(lambda x: [user["email"]
                        for user in x], rezultati))
        usernames = list(
            map(lambda x: [user["username"] for user in x], rezultati))
        print(f"Imena: \n {imena}")
        print(f"Emailovi: \n {emailovi}")
        print(f"Usernameovi: \n {usernames}")

        print(f"Ukupno vrijeme: {time.time() - start_time:.2f}")


asyncio.run(main())
