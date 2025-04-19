from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time
from .Routers import users, movies, jwtoauth2


app = FastAPI(title="FastAPI - Movies API",
            description="API para gestionar una base de datos de películas",
            version="1.0.0",
            ) 
app.include_router(users.router)
app.include_router(movies.router)
app.include_router(jwtoauth2.router)
#--------------------------------------------------------- CORS --------------------------------------------------------------

origins = [
    "http://localhost",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#--------------------------------------------------------- Middleware --------------------------------------------------------------
@app.middleware("http")
async def add_procces_time_sleep(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Request {request.url} completed in {process_time:.2f} seconds")
    response.headers["X-Process-Time"] = str(process_time)
    return response

#--------------------------------------------------------- Endpoints --------------------------------------------------------------
@app.get("/") 
def read_root():
    return {"message": "Hello World"}