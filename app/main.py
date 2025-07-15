from fastapi import FastAPI
from app.routers import users, tasks
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS config
origins = [
    "https://task-manager-frontend-rose-gamma.vercel.app",  # frontend dev en Vite
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # puedes usar ["*"] si estás en desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Rutas
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def root():
    return {"message": "Task Manager API is running!"}
