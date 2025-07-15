from fastapi import FastAPI
from app.routers import users, tasks

app = FastAPI()

# Rutas
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def root():
    return {"message": "Task Manager API is running!"}
