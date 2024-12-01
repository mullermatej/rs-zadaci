import asyncio
import aiohttp
from aiohttp import web

app = web.Application()

proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

narudzbe = []


async def dohvati_proizvode(request):
    return web.json_response(proizvodi)


async def dohvati_proizvod(request):
    id = request.match_info.get("id")
    print("ID:", id)
    if id is None:
        return web.json_response({"error": "Proizvod s traženim ID-em ne postoji"}, status=404)

    for proizvod in proizvodi:
        if proizvod["id"] == int(id):
            return web.json_response(proizvod)

    return web.json_response({"error": "Proizvod s traženim ID-em ne postoji"}, status=404)


async def dohvati_narudzbu(request):
    narudzba = await request.json()

    for proizvod in proizvodi:
        if proizvod["id"] == narudzba["proizvod_id"]:
            for i in range(narudzba["kolicina"]):
                narudzbe.append(proizvod)
            return web.json_response(narudzbe, status=201)

    return web.json_response("Proizvod s traženim ID-em ne postoji", status=404)

app.router.add_get("/proizvodi", dohvati_proizvode)
app.router.add_get("/proizvodi/{id}", dohvati_proizvod)
app.router.add_post("/narudzba", dohvati_narudzbu)


web.run_app(app, host="localhost", port=8081)
