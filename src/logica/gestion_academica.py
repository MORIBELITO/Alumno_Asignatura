from src.modelo.alumno import Alumno
from src.modelo.asignatura import Asignatura
from src.modelo.declarative_base import engine, Base, session


class GestionAcademica:
    def __init__(self):
        Base.metadata.create_all(engine)

    @staticmethod
    def agregar_alumno(nombre, edad):
        busqueda = session.query(Alumno).filter(Alumno.nombre == nombre).all()
        if len(busqueda) == 0:
            alumno = Alumno(nombre=nombre, edad=edad)
            session.add(alumno)
            session.commit()
            return True
        else:
            return False

    @staticmethod
    def editar_alumno(alumno_id, nombre, edad):
        busqueda = session.query(Alumno).filter(Alumno.nombre == nombre, Alumno.id != alumno_id).all()
        if len(busqueda) == 0:
            alumno = session.query(Alumno).filter(Alumno.id == alumno_id).first()
            alumno.nombre = nombre
            alumno.edad = edad
            session.commit()
            return True
        else:
            return False

    @staticmethod
    def dar_alumno_por_id(alumno_id):
        return session.query(Alumno).get(alumno_id).__dict__

    @staticmethod
    def agregar_asignatura(nombre, descripcion):
        busqueda = session.query(Asignatura).filter(Asignatura.nombre == nombre).all()
        if len(busqueda) == 0:
            asignatura = Asignatura(nombre=nombre, descripcion=descripcion)
            session.add(asignatura)
            session.commit()
            return True
        else:
            return False

    @staticmethod
    def editar_asignatura(asignatura_id, nombre, descripcion):
        busqueda = session.query(Asignatura).filter(Asignatura.nombre == nombre, Asignatura.id != asignatura_id).all()
        if len(busqueda) == 0:
            asignatura = session.query(Asignatura).filter(Asignatura.id == asignatura_id).first()
            asignatura.nombre = nombre
            asignatura.descripcion = descripcion
            session.commit()
            return True
        else:
            return False

    @staticmethod
    def dar_asignatura_por_id(asignatura_id):
        return session.query(Asignatura).get(asignatura_id).__dict__
