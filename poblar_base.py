from datetime import date

from sqlalchemy.orm import sessionmaker

from crear_base_entidades import engine, Clinica, Consultorio, Veterinario, \
    HistoriaClinica

Session = sessionmaker(bind=engine)
session = Session()

# ---------------- Clínicas ----------------
c1 = Clinica(nombre_comercial="VetSalud Loja", direccion="Av. Universitaria y Mercadillo, Loja",
             veterinario_responsable="Carlos Jaramillo")
c2 = Clinica(nombre_comercial="Patitas Felices", direccion="Av. Amazonas N24-12, Quito",
             veterinario_responsable="María Andrade")
c3 = Clinica(nombre_comercial="Clínica Animal Guayas", direccion="Av. 9 de Octubre 410, Guayaquil",
             veterinario_responsable="Luis Mendoza")

# ---------------- Consultorios ----------------
co1 = Consultorio(nombre="Consultorio 101", especialidad="Medicina general", clinica=c1)
co2 = Consultorio(nombre="Consultorio 102", especialidad="Cirugía", clinica=c1)
co3 = Consultorio(nombre="Consultorio A", especialidad="Dermatología", clinica=c2)
co4 = Consultorio(nombre="Consultorio B", especialidad="Medicina general", clinica=c2)
co5 = Consultorio(nombre="Consultorio 1", especialidad="Cardiología", clinica=c3)

# ---------------- Veterinarios ----------------
v1 = Veterinario(nombres="Ana", apellidos="Torres", correo="ana.torres@vetsalud.ec",
                 licencia="LIC-1001", consultorio=co1)
v2 = Veterinario(nombres="Pedro", apellidos="Castillo", correo="pedro.castillo@vetsalud.ec",
                 licencia="LIC-1002", consultorio=co2)
v3 = Veterinario(nombres="Lucía", apellidos="Ramírez", correo="lucia.ramirez@patitas.ec",
                 licencia="LIC-2001", consultorio=co3)
v4 = Veterinario(nombres="Jorge", apellidos="Vega", correo="jorge.vega@patitas.ec",
                 licencia="LIC-2002", consultorio=co4)
v5 = Veterinario(nombres="Sofía", apellidos="Cedeño", correo="sofia.cedeno@animalguayas.ec",
                 licencia="LIC-3001", consultorio=co5)

# ---------------- Historias clínicas ----------------
historias = [
    HistoriaClinica(fecha_atencion=date(2026, 9, 3), diagnostico="Parasitosis intestinal",
                    tratamiento="Desparasitante oral", nombre_mascota="Firulais", veterinario=v1),
    HistoriaClinica(fecha_atencion=date(2026, 9, 10), diagnostico="Otitis externa",
                    tratamiento="Gotas óticas por 7 días", nombre_mascota="Luna", veterinario=v1),
    HistoriaClinica(fecha_atencion=date(2026, 9, 15), diagnostico="Fractura de pata",
                    tratamiento="Cirugía y reposo", nombre_mascota="Rocky", veterinario=v2),
    HistoriaClinica(fecha_atencion=date(2026, 10, 1), diagnostico="Dermatitis alérgica",
                    tratamiento="Antihistamínico y champú medicado", nombre_mascota="Michi", veterinario=v3),
    HistoriaClinica(fecha_atencion=date(2026, 10, 5), diagnostico="Sarna",
                    tratamiento="Baños medicados", nombre_mascota="Toby", veterinario=v3),
    HistoriaClinica(fecha_atencion=date(2026, 10, 12), diagnostico="Gastroenteritis",
                    tratamiento="Dieta blanda e hidratación", nombre_mascota="Max", veterinario=v4),
    HistoriaClinica(fecha_atencion=date(2026, 10, 20), diagnostico="Soplo cardíaco",
                    tratamiento="Control y medicación cardíaca", nombre_mascota="Nina", veterinario=v5),
    HistoriaClinica(fecha_atencion=date(2026, 11, 2), diagnostico="Vacunación anual",
                    tratamiento="Vacuna séxtuple", nombre_mascota="Bobby", veterinario=v1),
]

# Al agregar las clínicas se guardan en cascada consultorios, veterinarios e historias
session.add_all([c1, c2, c3])
session.add_all(historias)

session.commit()
print("Datos ingresados correctamente")
