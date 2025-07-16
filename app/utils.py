import os
import json
from dotenv import load_dotenv
from google.cloud import firestore
from google.oauth2 import service_account

# Cargar .env local (opcional en producción)
load_dotenv()

# Cargar credenciales como texto JSON desde variable de entorno
credentials_json = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")
if not credentials_json:
    raise ValueError("Falta la variable GOOGLE_APPLICATION_CREDENTIALS_JSON")

info = json.loads(credentials_json)
creds = service_account.Credentials.from_service_account_info(info)

# Leer project_id si lo necesitas
project_id = os.getenv("PROJECT_ID")

# Inicializar Firestore con parámetros explícitos
db = firestore.Client(project=project_id, credentials=creds)
