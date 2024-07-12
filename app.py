import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from model import Usuario

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

logging.basicConfig(level=logging.INFO)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email e senha são obrigatórios'}), 400

    try:
        usuario = Usuario(email, password)
        user_record = usuario.criar()
        return jsonify({'message': 'Usuário criado com sucesso', 'uid': user_record.uid}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logging.error("Erro ao criar usuário: %s", str(e))
        return jsonify({'error': 'Erro ao criar usuário'}), 500

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    id_token = data.get('idToken')

    if not id_token:
        return jsonify({'error': 'Token de autenticação é obrigatório'}), 400

    try:
        usuario = Usuario(email=None, password=None)
        decoded_token = usuario.autenticar(id_token)
        return jsonify({'message': 'Usuário autenticado com sucesso', 'uid': usuario.uid}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logging.error("Erro de autenticação: %s", str(e))
        return jsonify({'error': 'Erro de autenticação'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)
