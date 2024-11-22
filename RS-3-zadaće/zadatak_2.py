import asyncio


async def main():
    await asyncio.gather(korisnici(), proizvodi())
    return


async def korisnici():
    korisnici = [{'ime': 'Ivan', 'prezime': 'Ivić'},
                 {'ime': 'Mate', 'prezime': 'Matić'},
                 {'ime': 'Ana', 'prezime': 'Anić'}]
    await asyncio.sleep(3)
    print(korisnici)
    return korisnici


async def proizvodi():
    proizvodi = [{'proizvod': 'jabuka', 'cijena': 5},
                 {'proizvod': 'kruška ', 'cijena': 6},
                 {'proizvod': 'banana', 'cijena': 7}]
    await asyncio.sleep(5)
    print(proizvodi)
    return proizvodi

asyncio.run(main())
