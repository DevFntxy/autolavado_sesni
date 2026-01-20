#model.py
from typing import List,Optional
from uuid import UUID, uuid4 
from pydantic import BaseModel, Field
from enum import Enum

class Genero (str, Enum):
    MASCULINO = "Hombre"
    FEMENINO = "Mujer"
    OTRO = "Otro"

class Rol (str, Enum):
    ADMIN = "Admin"
    USER = "User"
    
class Usuario (BaseModel):
    id: Optional[UUID] =uuid4()
    primerNombre : str
    apellido : str
    genero : Genero
    rol: List[Rol]