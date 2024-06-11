from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .declarative_base import Base


class Asignatura(Base):
    __tablename__ = 'asignatura'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)
    alumnos = relationship('Alumno', secondary='alumno_asignatura')
