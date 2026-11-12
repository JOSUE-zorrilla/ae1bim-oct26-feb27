from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# Se importa la cadena de conexión desde el archivo de configuración
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Base = declarative_base()


class Clinica(Base):
    """Unidad de atención donde se prestan servicios médicos para mascotas."""
    __tablename__ = 'clinica'

    id = Column(Integer, primary_key=True)
    nombre_comercial = Column(String(100), nullable=False)
    direccion = Column(String(200), nullable=False)
    veterinario_responsable = Column(String(100), nullable=False)

    # Una clínica tiene muchos consultorios
    consultorios = relationship("Consultorio", back_populates="clinica")

    def __repr__(self):
        return "Clinica: id=%d nombre=%s direccion=%s responsable=%s" % (
            self.id, self.nombre_comercial, self.direccion,
            self.veterinario_responsable)


class Consultorio(Base):
    """Consultorio asociado obligatoriamente a una sola clínica."""
    __tablename__ = 'consultorio'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)        # nombre o número
    especialidad = Column(String(100), nullable=False)  # medicina general, cirugía...
    clinica_id = Column(Integer, ForeignKey('clinica.id'), nullable=False)

    clinica = relationship("Clinica", back_populates="consultorios")
    veterinarios = relationship("Veterinario", back_populates="consultorio")

    def __repr__(self):
        return "Consultorio: id=%d nombre=%s especialidad=%s clinica_id=%d" % (
            self.id, self.nombre, self.especialidad, self.clinica_id)


class Veterinario(Base):
    """Veterinario que pertenece únicamente a un consultorio."""
    __tablename__ = 'veterinario'

    id = Column(Integer, primary_key=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(100), nullable=False, unique=True)
    licencia = Column(String(30), nullable=False, unique=True)
    consultorio_id = Column(Integer, ForeignKey('consultorio.id'), nullable=False)

    consultorio = relationship("Consultorio", back_populates="veterinarios")
    historias = relationship("HistoriaClinica", back_populates="veterinario")

    def __repr__(self):
        return "Veterinario: id=%d %s %s correo=%s licencia=%s" % (
            self.id, self.nombres, self.apellidos, self.correo, self.licencia)


class HistoriaClinica(Base):
    """Historia clínica asociada obligatoriamente al veterinario que la elaboró."""
    __tablename__ = 'historia_clinica'

    id = Column(Integer, primary_key=True)
    fecha_atencion = Column(Date, nullable=False)
    diagnostico = Column(String(200), nullable=False)
    tratamiento = Column(String(200), nullable=False)
    nombre_mascota = Column(String(100), nullable=False)
    veterinario_id = Column(Integer, ForeignKey('veterinario.id'), nullable=False)

    veterinario = relationship("Veterinario", back_populates="historias")

    def __repr__(self):
        return "HistoriaClinica: id=%d fecha=%s mascota=%s diagnostico=%s" % (
            self.id, self.fecha_atencion, self.nombre_mascota, self.diagnostico)


# Crea todas las tablas en la base de datos
Base.metadata.create_all(engine)
