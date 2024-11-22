import asyncio
import random


async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    if broj % 2 == 0:
        return f"Broj {broj} je paran."
    else:
        return f"Broj {broj} je neparan."


async def main():
    print("Provjeravam parnost nasumičnih brojeva...")
    lista_brojeva = [random.randint(1, 100) for _ in range(10)]

    zadaci = [asyncio.create_task(provjeri_parnost(broj))
              for broj in lista_brojeva]

    rezultati = await asyncio.gather(*zadaci)

    print("\n".join(rezultati))


asyncio.run(main())
