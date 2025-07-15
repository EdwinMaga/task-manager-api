from fastapi import APIRouter, Depends, HTTPException
from app.auth import get_current_user
from app.models import TaskCreate, TaskOut
from app.services import task_service

router = APIRouter()

@router.post("/", status_code=201)
def create_task(task: TaskCreate, user: str = Depends(get_current_user)):
    task_id = task_service.create_task(user, task.dict())
    return {"message": "Tarea creada", "task_id": task_id}

@router.get("/", response_model=list[TaskOut])
def list_tasks(user: str = Depends(get_current_user)):
    return task_service.get_tasks(user)

@router.patch("/{task_id}/done")
def complete_task(task_id: str, user: str = Depends(get_current_user)):
    success = task_service.mark_task_done(user, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"message": "Tarea marcada como completada"}

@router.delete("/{task_id}")
def delete_task(task_id: str, user: str = Depends(get_current_user)):
    success = task_service.delete_task(user, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"message": "Tarea eliminada"}