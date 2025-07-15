from app.utils import db
from datetime import datetime
from google.cloud import firestore

def create_task(email: str, data: dict):
    task_ref = db.collection("users").document(email).collection("tasks").document()
    task_ref.set({
        "title": data["title"],
        "description": data.get("description"),
        "done": False,
        "created_at": datetime.utcnow()
    })
    return task_ref.id

def get_tasks(email: str):
    tasks_ref = db.collection("users").document(email).collection("tasks")
    docs = tasks_ref.order_by("created_at", direction=firestore.Query.DESCENDING).stream()
    return [{"id": doc.id, **doc.to_dict()} for doc in docs]

def mark_task_done(email: str, task_id: str):
    ref = db.collection("users").document(email).collection("tasks").document(task_id)
    if not ref.get().exists:
        return False
    ref.update({"done": True})
    return True

def delete_task(email: str, task_id: str):
    ref = db.collection("users").document(email).collection("tasks").document(task_id)
    if not ref.get().exists:
        return False
    ref.delete()
    return True
