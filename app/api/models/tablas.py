from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Dominio(Base):
    __tablename__ = 'Dominio'
    idDominio = Column(Integer, primary_key=True)
    nombreDominio = Column(String(100), nullable=False)
    reinos = relationship("Reino", back_populates="dominio")

class Reino(Base):
    __tablename__ = 'Reino'
    idReino = Column(Integer, primary_key=True)
    nombreReino = Column(String(100), nullable=False)
    idDominio = Column(Integer, ForeignKey('Dominio.idDominio'))
    dominio = relationship("Dominio", back_populates="reinos")
    seres_vivos = relationship("SerVivo", back_populates="reino")

class SerVivo(Base):
    __tablename__ = 'SeresVivos'
    idSerVivo = Column(Integer, primary_key=True)
    nombreSerVivo = Column(String(100), nullable=False)
    tipo = Column(String(100))
    descripcion =Column(String(300))
    idReino = Column(Integer, ForeignKey('Reino.idReino'))
    reino = relationship("Reino", back_populates="seres_vivos")
