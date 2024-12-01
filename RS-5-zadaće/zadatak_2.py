import asyncio
import aiohttp
from aiohttp import web

app = web.Application()

proizvodi = [{"naziv": "banana", "kolicina": 5, "cijena": 2},
             {"naziv": "jabuka", "kolicina": 3, "cijena": 1}]


async def dohvati_proizvode(request):
    return web.json_response(proizvodi)


async def dodaj_proizvod(request):
    data = await request.json()
    print("Primljeni podaci: ", data)
    proizvodi.append(data)
    return web.json_response(proizvodi)


app.router.add_get("/proizvodi", dohvati_proizvode)
app.router.add_post("/proizvodi", dodaj_proizvod)


web.run_app(app, host="localhost", port=8081)
