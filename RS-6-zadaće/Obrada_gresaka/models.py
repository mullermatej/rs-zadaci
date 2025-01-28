from pydantic import BaseModel


class BaseCar(BaseModel):
    pass


class CreateCar(BaseCar):
    id: int
    marka: str
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str


class ResponseCar(BaseCar):
    id: int
