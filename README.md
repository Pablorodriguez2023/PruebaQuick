# PruebaQuick

## Superuser:
- user: admin
- password: admin

## Versiones:

- asgiref==3.7.2
- backports.zoneinfo==0.2.1
- certifi==2024.2.2
- charset-normalizer==3.3.2
- Django==4.2.11
- djangorestframework==3.15.0
- idna==3.6
- PyJWT==2.8.0
- requests==2.31.0
- sqlparse==0.4.4
- typing-extensions==4.10.0
- urllib3==2.2.1
- python==3.8.10
- pip==20.0.2

## Instrucciones de Uso:

### 1) Registrar Usuario Nuevo:
- **URL:** localhost:8000/registro-usuario
- **Campos:**
  ```json
  {
    "username": "nombre de usuario",
    "email": "correo electronico",
    "password": "contraseña"
  }

### 2) Iniciar Sesión:
- **URL:** localhost:8000/iniciar-sesion
- **Campos:**
  ```json
  {
    "username": "nombre de usuario",
    "email": "correo electronico",
    "password": "contraseña"
  }

### 3) Realizar Operaciones CRUD a los Modelos Solicitados:
- **URL:** localhost:8000/clientes
- **URL:** localhost:8000/facturas
- **URL:** localhost:8000/productos
- **URL:** localhost:8000/productosFactura

  
### 4) Descargar Archivo CSV de los Clientes Registrados:
- **URL:** localhost:8000/descargar-csv

### 5) Cargar Archivo CSV para el modelo clientes:
- **URL:** localhost:8000/cargar-csv-clientes
- Instrucciones: Ingresar la ruta específica del archivo CSV.



  






