from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.models import UserRegister, UserLogin, Token
from app.services.user_service import register_user, login_user

router = APIRouter()

@router.post("/register", status_code=201)
def register(user: UserRegister):
    user_id = register_user(user.email, user.password)
    if not user_id:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    return {"message": "Usuario registrado", "user_id": user_id}

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    token = login_user(form_data.username, form_data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {"access_token": token}
