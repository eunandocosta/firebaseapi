# FirebaseAPI - API para Gerenciamento de Usuários com Firebase

## Descrição

FirebaseAPI é uma API desenvolvida para gerenciar usuários utilizando Firebase Authentication. A API permite registrar novos usuários e autenticar usuários existentes através de tokens do Firebase.

## Tecnologias Utilizadas

- **Flask**: Framework de micro serviços para construção de APIs em Python.
- **Firebase Admin SDK**: Para integração com Firebase Authentication.
- **Docker**: Para containerização da aplicação.
- **Docker Compose**: Para orquestração dos containers.

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação Flask.
- `model.py`: Contém a classe `Usuario` para criação e autenticação de usuários.
- `firebase_app.py`: Inicialização do Firebase Admin SDK.
- `requirements.txt`: Arquivo com as dependências do projeto.
- `Dockerfile`: Arquivo para construir a imagem Docker da aplicação.
- `docker-compose.yml`: Arquivo de configuração do Docker Compose.
- `credentials/service_account_key.json`: Arquivo JSON com as credenciais do Firebase.

## Instalação

### Pré-requisitos

- Docker e Docker Compose instalados na sua máquina.
- Credenciais do Firebase (arquivo JSON).

### Passos para Configuração

1. Clone o repositório:

    ```bash
    git clone https://github.com/eunandocosta/firebaseapi.git
    cd firebaseapi
    ```

2. Coloque o arquivo JSON das credenciais do Firebase no diretório `credentials/` e renomeie para `service_account_key.json`.

3. Inicie os containers Docker:

    ```bash
    docker-compose up --build
    ```

4. A aplicação estará disponível em `http://localhost:5004`.

## Endpoints

### Registrar Usuário

- **URL**: `/register`
- **Método**: `POST`
- **Descrição**: Registra um novo usuário no Firebase Authentication.
- **Corpo da Requisição**:
    ```json
    {
        "email": "usuario@example.com",
        "password": "senha123"
    }
    ```
- **Exemplo de Resposta**:
    ```json
    {
        "message": "Usuário criado com sucesso",
        "uid": "UID_DO_USUARIO"
    }
    ```

### Autenticar Usuário

- **URL**: `/login`
- **Método**: `POST`
- **Descrição**: Autentica um usuário existente no Firebase Authentication usando um token de ID.
- **Corpo da Requisição**:
    ```json
    {
        "idToken": "TOKEN_DE_ID_DO_USUARIO"
    }
    ```
- **Exemplo de Resposta**:
    ```json
    {
        "message": "Usuário autenticado com sucesso",
        "uid": "UID_DO_USUARIO"
    }
    ```

## Utilizando Firebase Admin SDK

O Firebase Admin SDK é utilizado para criar e autenticar usuários. É necessário configurar as credenciais do Firebase para que o SDK possa se comunicar com o Firebase Authentication.

### Passos para obter as credenciais do Firebase:

1. Acesse [Firebase Console](https://console.firebase.google.com/).
2. Selecione o projeto desejado.
3. Navegue até **Configurações do Projeto > Contas de Serviço**.
4. Clique em **Gerar nova chave privada** e faça o download do arquivo JSON.
5. Coloque o arquivo JSON no diretório `credentials/` e renomeie para `service_account_key.json`.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.
