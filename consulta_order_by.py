from sqlalchemy.orm import sessionmaker

from crear_base_entidades import engine, HistoriaClinica, Veterinario

Session = sessionmaker(bind=engine)
session = Session()

# Uso de order_by(): historias clínicas ordenadas por fecha (más reciente primero)
historias = session.query(HistoriaClinica).order_by(
    HistoriaClinica.fecha_atencion.desc()).all()

print("Historias clínicas ordenadas por fecha de atención (descendente)")
for h in historias:
    print("%s | %s | %s | atendido por %s %s" % (
        h.fecha_atencion, h.nombre_mascota, h.diagnostico,
        h.veterinario.nombres, h.veterinario.apellidos))

# Otro ejemplo: veterinarios ordenados alfabéticamente por apellido
print("\nVeterinarios ordenados por apellido")
for v in session.query(Veterinario).order_by(Veterinario.apellidos).all():
    print("%s %s - %s" % (v.apellidos, v.nombres, v.consultorio.nombre))
