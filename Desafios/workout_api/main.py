from fastapi import FastAPI
from controllers import metodos

app = FastAPI()
app.include_router(metodos.router)