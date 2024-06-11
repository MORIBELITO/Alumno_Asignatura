from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .declarative_base import Base


class Alumno(Base):
    __tablename__ = 'alumno'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    edad = Column(Integer)
    asignaturas = relationship('Asignatura', secondary='alumno_asignatura')
