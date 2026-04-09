# First-term-exam---Practical

Este proyecto consiste en el diseño e implementación de una API REST orientada al aprendizaje de vulnerabilidades de autenticación. Incluye un módulo CRUD completo y un script de experimentación para auditoría de seguridad mediante fuerza bruta.

## Objetivo
Comprender el ciclo de vida de un ataque de fuerza bruta, medir su impacto en un entorno controlado y diseñar estrategias de mitigación proactivas.

## Stack Tecnologico
- Backend: FastAPI (Python 3.12+)
- Validacion de Datos: Pydantic
- Base de Datos: SQLite (Persistencia local)
- Servidor ASGI: Uvicorn

## Estructura del Proyecto
- main.py: Servidor API con endpoints de usuarios y logica de autenticacion.
- brute_force_lab.py: Script de experimentacion de fuerza bruta.
- Fuerzadb.db: Base de datos SQLite (se genera automaticamente).
- requirements.txt: Listado de dependencias.

## Configuracion del Entorno

1. Crear entorno virtual:
   python3 -m venv venv

2. Activar el entorno:
   source venv/bin/activate  # En Linux/Ubuntu
   # venv\Scripts\activate  # En Windows

3. Instalar dependencias:
   pip install fastapi uvicorn pydantic requests

## Ejecucion de la API

Inicie el servidor con el siguiente comando:
uvicorn main:app --reload

La documentacion interactiva (Swagger UI) estara disponible en: http://127.0.0.1:8000/docs

### Endpoints Principales
- POST /users: Registro de nuevos usuarios.
- GET /users: Listado de usuarios registrados.
- POST /login: Punto de entrada para validacion de credenciales.
- DELETE /users/{id}: Eliminacion de registros.

## Experimento de Fuerza Bruta

Para ejecutar la prueba de seguridad:
1. Asegurarse de que la API este en ejecucion.
2. Crear un usuario de prueba (ej: usuario 'admin' con clave 'password').
3. Ejecutar el script de prueba:
   python brute_force_lab.py


