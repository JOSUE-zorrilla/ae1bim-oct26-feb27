from sqlalchemy.orm import sessionmaker

from crear_base_entidades import engine, Consultorio

Session = sessionmaker(bind=engine)
session = Session()

# Uso de filter(): consultorios cuya especialidad es "Medicina general"
consultorios = session.query(Consultorio).filter(
    Consultorio.especialidad == "Medicina general").all()

print("Consultorios de Medicina general")
for c in consultorios:
    print("%s - clínica: %s" % (c.nombre, c.clinica.nombre_comercial))
