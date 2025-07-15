from app.utils import db
from app.auth import hash_password, verify_password, create_access_token

def get_user_by_email(email: str):
    users = db.collection("users")
    query = users.where("email", "==", email).limit(1).get()
    return query[0] if query else None

def register_user(email: str, password: str):
    if get_user_by_email(email):
        return None  # ya existe

    hashed_pw = hash_password(password)
    user_ref = db.collection("users").document()
    user_ref.set({"email": email, "password": hashed_pw})
    return user_ref.id

def login_user(email: str, password: str):
    user_doc = get_user_by_email(email)
    if not user_doc:
        return None
    user_data = user_doc.to_dict()
    if not verify_password(password, user_data["password"]):
        return None
    token = create_access_token({"sub": email})
    return token
