from fastapi import FastAPI, HTTPException, Query

from models import BaseCar, CreateCar, ResponseCar

app = FastAPI()

automobili = [
    {"id": 1, "marka": "BMW", "model": "420d",
        "godina_proizvodnje": 2016, "cijena": 25.000, "boja": "bijela"},
    {"id": 2, "marka": "Audi", "model": "A4",
     "godina_proizvodnje": 2017, "cijena": 23.000, "boja": "crna"},
    {"id": 3, "marka": "VW", "model": "Golf",
        "godina_proizvodnje": 2018, "cijena": 20.000, "boja": "siva"}
]


@app.get("/automobili/{id}", response_model=BaseCar)
def get_automobili(id: int = 1, min_cijena: float = Query(None, gt=0), max_cijena: float = None, min_godina: int = Query(None, gt=1960), max_godina: int = None):
    if (min_cijena is not None and max_cijena is not None) and (min_cijena > max_cijena) or (min_godina is not None and max_godina is not None) and (min_godina > max_godina):
        raise HTTPException(
            status_code=400, detail="Neispravni query parametri")
    for automobil in automobili:
        if automobil["id"] == id:
            return automobil
    raise HTTPException(status_code=404, detail="Automobil nije pronadjen")


@app.post("/automobili", response_model=ResponseCar)
def post_automobili(automobil: CreateCar):
    new_id = len(automobili) + 1
    automobil_s_id: CreateCar = {"id": new_id, **automobil.model_dump()}
    automobili.append(automobil_s_id)
    return automobili
