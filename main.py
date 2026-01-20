from  fastapi import FastAPI
from typing import List,Optional
from uuid import UUID, uuid4 
from model import Usuario, Genero, Rol

app = FastAPI()

db: List[Usuario] = [
    Usuario(
        id=uuid4(),
        primerNombre="Derek",
        apellido="Sesni",
        genero=Genero.MASCULINO,
        rol=[Rol.ADMIN]
    ),
        Usuario(
        id=uuid4(),
        primerNombre="Mati",
        apellido="Grani",
        genero=Genero.MASCULINO,
        rol=[Rol.USER]
    ),
        Usuario(
        id=uuid4(),
        primerNombre="Diego",
        apellido="Rivera",
        genero=Genero.MASCULINO,
        rol=[Rol.USER]
    ),
]

@app.get("/")
async def root():
    return {"message": "Hola soy Ses"}

@app.get("/api/v1/usuarios")
async def get_usuarios():
    return db