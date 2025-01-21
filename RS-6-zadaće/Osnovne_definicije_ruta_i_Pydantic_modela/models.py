from pydantic import BaseModel


class CreateFilm(BaseModel):
    naziv: str
    genre: str
    godina: int


class Film(BaseModel):
    id: int
    naziv: str
    genre: str
    godina: int
