from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API funcionando 🚀"}

@app.get("/hora")
def hora():
    return {"hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {"mensaje": f"Hola {nombre}, bienvenido a tu API"}
