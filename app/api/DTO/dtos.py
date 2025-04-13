from pydantic import BaseModel
from typing import Optional

class DominioDTO(BaseModel):
    idDominio: int
    nombreDominio: str
    class Config:
        orm_mode = True

class ReinoDTO(BaseModel):
    idReino: int
    nombreReino: str
    idDominio: int
    class Config:
        orm_mode = True

class SerVivoDTO(BaseModel):
    idSerVivo: int
    nombreSerVivo: str
    tipo: Optional[str]
    descripcion:str
    idReino: int
    class Config:
        orm_mode = True
