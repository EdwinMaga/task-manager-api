# 📌 Task Manager API

Una API REST para gestión de tareas personales, construida con **FastAPI** y **Firestore**.

## 🚀 Tecnologías

- FastAPI
- Firestore (Firebase)
- JWT (Autenticación)
- Python 3
- Uvicorn
- dotenv

## 🔐 Autenticación

La API utiliza JWT para proteger los endpoints. Debes iniciar sesión y usar el token para acceder a rutas como `/tasks`.

## 📚 Endpoints principales

### Usuarios
- `POST /users/register` → Registro
- `POST /users/login` → Login y generación de token

### Tareas (requieren token JWT)
- `POST /tasks/` → Crear tarea
- `GET /tasks/` → Obtener tareas
- `PATCH /tasks/{id}/done` → Marcar tarea como hecha
- `DELETE /tasks/{id}` → Eliminar tarea

## 🔧 Instalación

git clone https://github.com/edwinmaga/task-manager-api.git
cd task-manager-api
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requirements.txt