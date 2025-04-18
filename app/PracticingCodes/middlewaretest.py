import time
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Request {request.url} completed in {process_time:.2f} seconds")
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.get("/")
async def main():
    time_start = 500
    while time_start > 0:
        time_start-=10
        time.sleep(2)
        print(time_start)
    return {"message": "Hello World"}