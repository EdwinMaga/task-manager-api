import os
from dotenv import load_dotenv
from google.cloud import firestore
from google.oauth2 import service_account

# Cargar variables de entorno
load_dotenv()

project_id = os.getenv('PROJECT_ID')
database_name = os.getenv('DATABASE')
credentials = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Inicializar Firestore
db = firestore.Client(project=project_id, database=database_name, credentials=service_account.Credentials.from_service_account_file(credentials))