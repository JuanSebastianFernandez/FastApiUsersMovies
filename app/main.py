from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

app = FastAPI() 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
print(type(oauth2_scheme))

@app.get("/") 
def read_root():
    return {"message": "Hello World"}

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}