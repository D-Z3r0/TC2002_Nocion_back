from pydantic import BaseModel

class Tarea(BaseModel):
    id:int
    titulo:str
    descripcion:str
    fecha_c:str
    fecha_e:str
    tiempo:int