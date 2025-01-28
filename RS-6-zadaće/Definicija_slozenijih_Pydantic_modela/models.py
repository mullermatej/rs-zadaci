from pydantic import BaseModel
from typing import Optional, Literal, TypedDict, Tuple


class CCTV_frame(BaseModel):
    id: int
    vrijeme_snimanja: str
    koordinate: Optional[list[float, float]] = (0.0, 0.0)


class Jelo(BaseModel):
    id: int
    naziv: str
    cijena: float


class RestuarantOrder(BaseModel):
    id: int
    ime_kupca: str
    TypedDict("StolInfo", {"broj": int, "lokacija": str})
    lista_jela: list[str]
    ukupna_cijena: float


class Admin (BaseModel):
    ime: str
    prezime: str
    korisničko_ime: str
    email: str
    ovlasti: Literal["dodavanje", "brisanje", "ažuriranje", "čitanje"]


class Izdavač (BaseModel):
    naziv: str
    adresa: str


class Knjiga (BaseModel):
    naslov: str
    ime_autora: str
    prezime_autora: str
    godina_izdavanja: Optional[int] = 2025
    broj_stranica: int
    izdavač: Izdavač
