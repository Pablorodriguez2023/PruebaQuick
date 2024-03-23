import requests

import requests

def cargar_csv(url_api):
    ruta_archivo_csv = input("Ingrese la ruta completa del archivo CSV: ")
    try:
        with open(ruta_archivo_csv, 'rb') as archivo:
            archivos = {'archivo_csv': archivo}
            response = requests.post(url_api, files=archivos)
            if response.status_code == 200:
                print("El archivo CSV se cargó correctamente.")
            else:
                print(f"Error al cargar el archivo CSV: {response.text}")
    except FileNotFoundError:
        print("El archivo CSV no se encontró en la ruta especificada.")

if __name__ == "__main__":
    # URL de tu API de Django Rest Framework para cargar CSV
    url_api = 'http://localhost:8000/cargar-csv-clientes'

    cargar_csv(url_api)

    
    



def registrar_usuario(username, email, password):
    url = 'http://localhost:8000/registro-usuario'
    datos_usuario = {
        'username': username,
        'email': email,
        'password': password
    }
    
    # Enviar una solicitud POST al servidor
    respuesta = requests.post(url, json=datos_usuario)
    
    # Verificar si la solicitud fue exitosa
    if respuesta.status_code == 200:
        print("Usuario registrado exitosamente.")
    else:
        print("Error al registrar usuario. Código de estado:", respuesta.status_code)

if __name__ == "__main__":
    username = input("Ingrese su nombre: ")
    email = input("Ingrese su correo electrónico: ")
    password = input("Ingrese su contraseña: ")

    registrar_usuario(username, email, password)
    
    
