from sqlalchemy.orm import Session

from model import tareamodel
from schema import tareaschema

def create_tarea(db: Session, tarea: tareaschema.Tarea):
    db_tarea = tareamodel.Tarea(titulo=tarea.titulo,descripcion=tarea.descripcion,fecha_c=tarea.fecha_c,fecha_e=tarea.fecha_e,tiempo=tarea.tiempo)
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

def list_tareas(db:Session):
    tareas= db.query(tareamodel.Tarea).all()
    return tareas

def find_by_id(db:Session, id:int):
    tarea=db.query(tareamodel.Tarea).filter(tareamodel.Tarea.id==id).first()
    return tarea

def delete_tarea(db: Session, tarea_id: int):
    tarea = db.query(tareamodel.Tarea).filter(tareamodel.Tarea.id == tarea_id).first()
    if tarea:
        db.delete(tarea)
        db.commit()
        return tarea
    return None  # Devolver None si la tarea no se encontró o no se eliminó
