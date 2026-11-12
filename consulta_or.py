from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker

from crear_base_entidades import engine, Consultorio

Session = sessionmaker(bind=engine)
session = Session()

# Uso de or_(): consultorios de Dermatología O de Cirugía
consultorios = session.query(Consultorio).filter(
    or_(Consultorio.especialidad == "Dermatología",
        Consultorio.especialidad == "Cirugía")).all()

print("Consultorios de Dermatología o Cirugía")
for c in consultorios:
    print("%s - %s - clínica: %s" % (c.nombre, c.especialidad, c.clinica.nombre_comercial))
