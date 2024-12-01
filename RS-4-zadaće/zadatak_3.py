import aiohttp
import asyncio
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


async def get_dog_fact(session):
    print("Šaljem dog fact zahtjev")
    response = await session.get("https://dogapi.dog/api/v2/facts", ssl=ssl_context)
    fact_dict = await response.json()
    return fact_dict


async def get_cat_fact(session):
    print("Šaljem cat fact zahtjev")
    response = await session.get("https://catfact.ninja/fact", ssl=ssl_context)
    fact_dict = await response.json()
    return fact_dict


def mix_facts(dog_facts, cat_facts):
    mixed_facts = []
    for i in range(5):
        if (len(dog_facts[i]) > len(cat_facts[i])):
            mixed_facts.append(dog_facts[i])
        else:
            mixed_facts.append(cat_facts[i])

    return mixed_facts


async def main():
    async with aiohttp.ClientSession() as session:
        dog_facts_tasks = [asyncio.create_task(
            get_dog_fact(session)) for i in range(5)]
        cat_facts_tasks = [asyncio.create_task(
            get_cat_fact(session)) for i in range(5)]

        dog_cat_facts = await asyncio.gather(*dog_facts_tasks, *cat_facts_tasks)

        dog_facts = dog_cat_facts[:5]
        cat_facts = dog_cat_facts[5:]

        dog_facts = list(
            map(lambda x: x["data"][0]["attributes"]["body"], dog_facts))
        cat_facts = list(map(lambda x: x["fact"], cat_facts))

        mixed_facts = mix_facts(dog_facts, cat_facts)

        print("\nMixane činjenice o psima i mačkama:\n")
        print("\n".join(mixed_facts))

        # print("Dog Facts:")
        # for fact in dog_facts:
        #     print("-" + fact["data"][0]["attributes"]["body"])

        # print("\nCat Facts:")
        # for fact in cat_facts:
        #     print("-" + fact["fact"])


asyncio.run(main())
