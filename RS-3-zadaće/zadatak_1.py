import asyncio


async def dohvati_podatke():
    print("Dohvaćam podatke...")
    # lista = []
    # for i in range(1, 11):
    #     lista.append(i)
    lista = [i for i in range(1, 11)]
    await asyncio.sleep(3)
    print("Podaci dohvaćeni! : ", lista)
    return

asyncio.run(dohvati_podatke())
