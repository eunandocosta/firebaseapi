import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("credentials//service_account_key.json")
firebase_admin.initialize_app(cred)

