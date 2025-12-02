from pydantic import BaseModel

class ClienteBase(BaseModel):
    nome: str
    telefone: str
    email: str
    idade: int
    serviço_contratado: str


class Cliente(ClienteBase):
    id: int
