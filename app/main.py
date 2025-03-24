from fastapi import FastAPI   #Importamos la clase FastAPI desde el módulo fastapi

app = FastAPI() # Creamos una instancia de FastAPI y la guardamos en la variable app

@app.get("/") # Definimos una ruta o path con el decorador get que se refiere a una operación
def read_root():
    return {"message": "Hello World"}