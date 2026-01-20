from fastapi import FastAPI, HTTPException
from typing import List
from uuid import UUID, uuid4
from model import Usuario, Genero, Rol

app = FastAPI()

# Base de datos simulada
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

# ------------------ RUTA RAÍZ ------------------
@app.get("/")
async def root():
    return {"message": "Hola soy Ses"}

# ------------------ LISTAR USUARIOS ------------------
@app.get("/api/v1/usuarios", response_model=List[Usuario])
async def get_usuarios():
    return db

# ------------------ BUSCAR POR ID ------------------
@app.get("/api/v1/usuarios/{usuario_id}", response_model=Usuario)
async def get_usuario(usuario_id: UUID):
    for usuario in db:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# ------------------ CREAR USUARIO ------------------
@app.post("/api/v1/usuarios", response_model=Usuario)
async def crear_usuario(usuario: Usuario):
    usuario.id = uuid4()
    db.append(usuario)
    return usuario

# ------------------ ACTUALIZAR USUARIO ------------------
@app.put("/api/v1/usuarios/{usuario_id}", response_model=Usuario)
async def actualizar_usuario(usuario_id: UUID, usuario_actualizado: Usuario):
    for index, usuario in enumerate(db):
        if usuario.id == usuario_id:
            usuario_actualizado.id = usuario_id
            db[index] = usuario_actualizado
            return usuario_actualizado
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# ------------------ ELIMINAR USUARIO ------------------
@app.delete("/api/v1/usuarios/{usuario_id}")
async def eliminar_usuario(usuario_id: UUID):
    for index, usuario in enumerate(db):
        if usuario.id == usuario_id:
            db.pop(index)
            return {"message": "Usuario eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
