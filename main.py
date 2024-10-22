from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ["http://localhost:8081", "http://127.0.0.1:8081"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Usuario(BaseModel):
    nome: str
    idade: int

class UsuarioRead(Usuario):
    id: int

# Simulando dados para a lista
dados = [
    {"id": 1, "nome": "Bart", "foto": "data:image/jpeg;base64,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"},
    {"id": 2, "nome": "Homer", "foto": "data:image/png;base64,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"},
    {"id": 3, "nome": "Marge", "foto": "data:image/png;base64,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"}
]

@app.get("/itens")
async def obter_itens():
    return dados

@app.post("/usuarios")
async def salvar_usuario(usuario: Usuario):
    print(usuario)  # Adicione esta linha para ver se os dados estão chegando
    u = {
        "id": len(dados) + 1,
        "nome": usuario.nome,
        "idade": usuario.idade,
    }
    dados.append(u)
    return {"mensagem": "Usuário criado com sucesso!", "id": u["id"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
