from sqlalchemy.orm import sessionmaker

from crear_base_entidades import engine, Clinica

Session = sessionmaker(bind=engine)
session = Session()

# Uso de all(): todas las clínicas y, por cada una,
# el número de historias clínicas asociadas
# (Clínica -> Consultorios -> Veterinarios -> Historias Clínicas)
clinicas = session.query(Clinica).all()

print("Clínicas y número de historias clínicas asociadas")
for clinica in clinicas:
    total_historias = 0
    for consultorio in clinica.consultorios:
        for veterinario in consultorio.veterinarios:
            total_historias += len(veterinario.historias)
    print("%s -> %d historias clínicas" % (clinica.nombre_comercial, total_historias))
