import logging
from firebase_app import *

class Usuario:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.uid = None

    def criar(self):
        try:
            user_record = auth.create_user(
                email=self.email,
                password=self.password,
            )

            logging.info("Usuário criado com sucesso: %s", user_record.uid)
            return user_record

        except firebase_admin.auth.EmailAlreadyExistsError: 
            logging.warning("Este email já está cadastrado.")
            raise ValueError("Este email já está cadastrado.") 
        except Exception as error:  
            logging.error("Erro ao criar usuário: %s", error)
            raise error
    
    def autenticar(self, id_token): 
        try:
            decoded_token = auth.verify_id_token(id_token)
            self.uid = decoded_token['uid']
            logging.info("Usuário autenticado com sucesso: %s", self.uid)
            return decoded_token
        except auth.InvalidIdTokenError:
            raise ValueError("Token de autenticação inválido.")
        except Exception as e:  
            logging.error("Erro de autenticação: %s", str(e))
            raise ValueError(f"Erro de autenticação: {str(e)}")
