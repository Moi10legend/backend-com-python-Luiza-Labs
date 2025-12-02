from fastapi import FastAPI
from controllers import metodos

app = FastAPI(
    title="API de Atletas",
    description="API para cadastro e gerenciamento de atletas.",
    version="1.0.0"
)
app.include_router(metodos.router)