from sqlalchemy import Column, Integer, ForeignKey
from .declarative_base import Base


class AlumnoAsignatura(Base):
    __tablename__ = 'alumno_asignatura'
    alumno_id = Column(Integer, ForeignKey('alumno.id'), primary_key=True)
    asignatura_id = Column(Integer, ForeignKey('asignatura.id'), primary_key=True)
