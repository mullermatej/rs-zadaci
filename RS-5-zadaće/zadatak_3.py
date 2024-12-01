import asyncio
import aiohttp
from aiohttp import web

app = web.Application()

korisnici = [
    {'ime': 'Ivo', 'godine': 25},
    {'ime': 'Ana', 'godine': 17},
    {'ime': 'Marko', 'godine': 19},
    {'ime': 'Maja', 'godine': 16},
    {'ime': 'Iva', 'godine': 22}
]


async def punoljetni(request):
    punoljetni = [
        korisnik for korisnik in korisnici if korisnik['godine'] >= 18]
    return web.json_response(punoljetni)

app.router.add_get("/stariji_korisnici", punoljetni)


web.run_app(app, host="localhost", port=8082)
