from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base


class Tarea(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    descripcion = Column(String)
    fecha_c = Column(String)
    fecha_e = Column(String)
    tiempo = Column(Integer)
