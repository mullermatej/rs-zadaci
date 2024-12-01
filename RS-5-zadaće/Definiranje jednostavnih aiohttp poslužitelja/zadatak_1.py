import asyncio
import aiohttp
from aiohttp import web

app = web.Application()


async def dohvati_proizvode(request):
    proizvodi = [{"naziv": "banana", "kolicina": 5, "cijena": 2},
                 {"naziv": "jabuka", "kolicina": 3, "cijena": 1}]
    return web.json_response(proizvodi)


app.router.add_get("/proizvodi", dohvati_proizvode)

web.run_app(app, host="localhost", port=8081)
