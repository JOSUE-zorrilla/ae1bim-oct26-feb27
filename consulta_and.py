from datetime import date

from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker

from crear_base_entidades import engine, HistoriaClinica, Veterinario

Session = sessionmaker(bind=engine)
session = Session()

# Uso de and_(): historias clínicas atendidas en octubre de 2026
# Y elaboradas por la veterinaria con licencia LIC-2001
historias = session.query(HistoriaClinica).join(Veterinario).filter(
    and_(HistoriaClinica.fecha_atencion >= date(2026, 10, 1),
         HistoriaClinica.fecha_atencion <= date(2026, 10, 31),
         Veterinario.licencia == "LIC-2001")).all()

print("Historias de octubre 2026 del veterinario con licencia LIC-2001")
for h in historias:
    print("%s | %s | %s | %s" % (h.fecha_atencion, h.nombre_mascota,
                                  h.diagnostico, h.tratamiento))
