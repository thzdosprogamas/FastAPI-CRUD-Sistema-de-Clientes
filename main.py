from fastapi import FastAPI, HTTPException
from models import Cliente, ClienteBase

app = FastAPI()

# Banco de dados temporário
clientes = []

@app.get("/clientes", response_model=list[Cliente])
def listar_clientes():
    return clientes

@app.get("/cliente/{cliente_id}", response_model=Cliente)
def cliente_expecifico(cliente_id: int):
    for cliente in clientes:
        if cliente.id == cliente_id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
@app.post("/cliente", response_model=Cliente)
def criar_cliente(novo_cliente: ClienteBase):
    cliente_id = len(clientes) + 1
    cliente = Cliente(id=cliente_id, **novo_cliente.dict())
    clientes.append(cliente)
    return cliente


@app.put("/cliente/{cliente_id}", response_model=Cliente)
def atualizar_informacoes(cliente_id: int, cliente_atualizado: Cliente):    
    for index, cliente in enumerate(clientes):
        if cliente.id == cliente_id:
         id_antigo = cliente.id
         dados = cliente_atualizado.dict()
         dados['id'] = id_antigo
         cliente_atualizado = Cliente(**dados)
         clientes[index] = cliente_atualizado
         return cliente_atualizado
    raise HTTPException(status_code=404, detail="Cliente não encontrado")


@app.delete("/cliente/{cliente_id}")
def deletar_cliente(cliente_id: int):
    for index, cliente in enumerate(clientes):
        if cliente.id == cliente_id:
            del clientes[index]
            return {"message": "Cliente deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Cliente não encontrado")
