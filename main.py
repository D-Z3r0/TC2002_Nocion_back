from fastapi import FastAPI,Depends
from schema.tareaschema import Tarea
from repository import tarearepository
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
async def print_hello():
    return {"message":"Conectado"}


# @app.get("/tareas")
# async def get_tareas(tarea:Tarea):
#     return {"message":"Tareas Obtenidas Exitosamente"}


# @app.post("/tarea_post)
# async def hello_name(user:User):
#     return {"message":f"Hello {user.name}"}

@app.post("/tarea/create",response_model=Tarea)
async def create_tarea(tarea:Tarea, db: Session = Depends(get_db)):
    tarea=tarearepository.create_tarea(db,tarea)
    return tarea

@app.get("/tarea/list",response_model=list[Tarea])
async def list_tareas(db: Session = Depends(get_db)):
    tareas=tarearepository.list_tareas(db)
    return tareas

@app.delete("/tarea/delete/{tarea_id}",response_model=Tarea)
async def delete_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = tarearepository.find_by_id(db, tarea_id)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tarearepository.delete_tarea(db, tarea_id)
    return tarea

# @app.get("/user/find/{id}",response_model=User)
# async def find_by_id(db:Session=Depends(get_db),id:int=0):
#     print(id)
#     user=userrepository.find_by_id(db,id)
#     print(user)
#     return user
