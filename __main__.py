from src.modelo.alumno import Alumno
from src.modelo.asignatura import Asignatura
from src.modelo.declarative_base import Session, engine, Base
from src.logica.gestion_academica import GestionAcademica

if __name__ == '__main__':
    # Crear la BD
    Base.metadata.create_all(engine)
    # Abrir la sesión
    session = Session()

    # Crear alumnos
    GestionAcademica.agregar_alumno('Juan Perez', 20)
    GestionAcademica.agregar_alumno('Maria Lopez', 22)
    GestionAcademica.agregar_alumno('Carlos Gomez', 21)

    # Crear asignaturas
    GestionAcademica.agregar_asignatura('Matemáticas', 'Álgebra y Cálculo')
    GestionAcademica.agregar_asignatura('Historia', 'Historia Universal')

    # Relacionar alumnos con asignaturas
    asignatura1 = session.query(Asignatura).filter_by(nombre='Matemáticas').first()
    asignatura2 = session.query(Asignatura).filter_by(nombre='Historia').first()

    alumno1 = session.query(Alumno).filter_by(nombre='Juan Perez').first()
    alumno2 = session.query(Alumno).filter_by(nombre='Maria Lopez').first()
    alumno3 = session.query(Alumno).filter_by(nombre='Carlos Gomez').first()

    asignatura1.alumnos = [alumno1, alumno2]
    asignatura2.alumnos = [alumno2, alumno3]

    session.commit()
    session.close()
