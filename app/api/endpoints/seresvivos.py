from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.api.models.tablas import Dominio, Reino, SerVivo
from app.api.DTO.dtos import DominioDTO, ReinoDTO, SerVivoDTO
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/dominios", response_model=List[DominioDTO])
def obtener_dominios(db: Session = Depends(get_db)):
    return db.query(Dominio).all()

@router.post("/dominios", response_model=DominioDTO)
def crear_dominio(dominio: DominioDTO, db: Session = Depends(get_db)):
    nuevo_dominio = Dominio(**dominio.dict())
    db.add(nuevo_dominio)
    db.commit()
    db.refresh(nuevo_dominio)
    return nuevo_dominio


@router.get("/reinos", response_model=List[ReinoDTO])
def obtener_reinos(db: Session = Depends(get_db)):
    return db.query(Reino).all()

@router.post("/reinos", response_model=ReinoDTO)
def crear_reino(reino: ReinoDTO, db: Session = Depends(get_db)):
    nuevo_reino = Reino(**reino.dict())
    db.add(nuevo_reino)
    db.commit()
    db.refresh(nuevo_reino)
    return nuevo_reino


@router.get("/seresvivos", response_model=List[SerVivoDTO])
def obtener_seres_vivos(db: Session = Depends(get_db)):
    return db.query(SerVivo).all()

@router.post("/seresvivos", response_model=SerVivoDTO)
def crear_ser_vivo(ser: SerVivoDTO, db: Session = Depends(get_db)):
    nuevo_ser = SerVivo(**ser.dict())
    db.add(nuevo_ser)
    db.commit()
    db.refresh(nuevo_ser)
    return nuevo_ser
