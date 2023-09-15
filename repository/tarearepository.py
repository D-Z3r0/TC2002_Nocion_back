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
    user=db.query(usermodel.User).filter(usermodel.User.id==id).first()
    return user