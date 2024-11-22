import asyncio

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]


async def main():
    await autentifikacija({'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com', "lozinka": "s324SDFfdsj234"})
    return


async def autentifikacija(korisnik):
    rezultat = False
    print("Pronalazim korisnika...")
    await asyncio.sleep(3)
    for rjecnik in baza_korisnika:
        if (rjecnik["korisnicko_ime"] == korisnik["korisnicko_ime"] and rjecnik["email"] == korisnik["email"]):
            await autorizacija(korisnik)
            rezultat = True
            return
    if rezultat == False:
        print(f"Korisnik {korisnik["korisnicko_ime"]} nije pronađen.")
        return


async def autorizacija(korisnik):
    print("Autoriziram korisnika...")
    await asyncio.sleep(2)
    for korisnik_data in baza_lozinka:
        if (korisnik_data["korisnicko_ime"] == korisnik["korisnicko_ime"] and korisnik_data["lozinka"] == korisnik["lozinka"]):
            print(f"Korisnik {
                  korisnik["korisnicko_ime"]}: Autorizacija uspješna.")
            return
    print(f"Korisnik {korisnik["korisnicko_ime"]}: Autorizacija neuspješna.")


asyncio.run(main())
