import aiohttp
import asyncio
import ssl


async def get_cat_fact(session, broj):
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    print(f"Šaljem zahtjev {broj}")
    response = await session.get("https://catfact.ninja/fact", ssl=ssl_context)
    fact_dict = await response.json()
    return fact_dict


def filter_cat_facts(facts):
    return [fact["fact"] for fact in facts if "cat" in fact["fact"].lower()]


async def main():
    async with aiohttp.ClientSession() as session:

        taskovi = [asyncio.create_task(get_cat_fact(session, i))
                   for i in range(20)]

        rezultati = await asyncio.gather(*taskovi)
        filtered_facts = filter_cat_facts(rezultati)
        print("Filtrirane činjenice o mačkama:\n" + "\n - ".join(filtered_facts))

asyncio.run(main())
