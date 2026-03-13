from fastapi import FastAPI
from routes.module_routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Fastapi server running"}
