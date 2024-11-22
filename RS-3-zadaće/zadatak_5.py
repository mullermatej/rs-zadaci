import asyncio


async def main():
    print("Enkriptiram podatke...")

    lista = [
        {"prezime": "Muller", "broj_kartice": "1234 5678 1234 5678", "CVV": "123"},
        {"prezime": "Marić", "broj_kartice": "1234 5678 1111 5678", "CVV": "456"},
        {"prezime": "Božić", "broj_kartice": "1234 5678 2222 5678", "CVV": "789"},
    ]

    zadaci = [asyncio.create_task(secure_data(rjecnik)) for rjecnik in lista]
    rezultati = await asyncio.gather(*zadaci)

    print("Zadaci: ", rezultati)


async def secure_data(rjecnik):
    await asyncio.sleep(3)
    return {"prezime": rjecnik["prezime"], "broj_kartice": hash(rjecnik["broj_kartice"]), "CVV": hash(rjecnik["CVV"])}

asyncio.run(main())
