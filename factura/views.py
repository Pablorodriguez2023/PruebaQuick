from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Cliente, Factura, Producto, ProductoFactura
from .serializers import ClienteSerializer, FacturaSerializer, ProductoSerializer, ProductoFacturaSerializer
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import jwt
from django.views import View
from django.conf import settings
import csv
from django.http import HttpResponse
from io import StringIO
from datetime import timedelta, datetime 
from django.http import JsonResponse
from urllib import request, parse
from django.utils import timezone



class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ProductoFacturaViewSet(viewsets.ModelViewSet):
    queryset = ProductoFactura.objects.all()
    serializer_class = ProductoFacturaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    


class RegistroUsuarioAPIView(APIView):
    def post(self, request, format=None):
        data = request.data

        if User.objects.filter(email=data.get('email')).exists():
            return Response({"error": "Ya existe un usuario con este correo electrónico"}, status=status.HTTP_400_BAD_REQUEST)

        nuevo_usuario = User.objects.create_user(username=data.get('username'), email=data.get('email'), password=data.get('password'))

        nuevo_usuario.save()

        return Response("Usuario registrado exitosamente", status=status.HTTP_201_CREATED)


class IniciarSesionAPIView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')
        usuario = authenticate(request,email=email, password=password)

        if usuario is not None:
               # Generar el token JWT
            token_payload = {
                'email': email,
                'exp': timezone.now() + timedelta(hours=1)  # Expira en 1 hora
            }
            token = jwt.encode(token_payload, settings.SECRET_KEY, algorithm='HS256')

            return Response({'token': token}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        
        
    def mi_vista(request):
        if request.method == 'POST':
            # URL de la vista IniciarSesionAPIView
            url = 'http://localhost:8000/iniciar-sesion'

            # Datos de inicio de sesión en formato JSON
            data = {
                "email": request.POST.get('email'),
                "password": request.POST.get('password')
            }

            # Codificar los datos como un string de consulta
            encoded_data = parse.urlencode(data).encode()

            # Realizar la solicitud POST
            req = request.Request(url, data=encoded_data)

            # Capturar la respuesta
            try:
                with request.urlopen(req) as response:
                    content = response.read()
                    # Procesar la respuesta como desees
                    # En este ejemplo, simplemente retornamos la respuesta como JSON
                    return JsonResponse({'response': content.decode()})
            except Exception as e:
                # Manejar cualquier excepción que pueda ocurrir durante la solicitud
                return JsonResponse({'error': str(e)})
        else:
            # Si no es una solicitud POST, se debe manejar adecuadamente
            return JsonResponse({'error': 'Método no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



class CargarCSVClientes(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        csv_file = request.FILES.get('archivo_csv')  # Utiliza get para manejar el caso de que no haya archivo
        if not csv_file:
            return Response("No se proporcionó ningún archivo CSV", status=status.HTTP_400_BAD_REQUEST)

        csv_data = csv.reader(csv_file.read().decode('utf-8').splitlines())
        errors = []

        for row in csv_data:
            if len(row) >= 4:
                documento, nombre, apellido, email = row
                Cliente.objects.create(documento=documento, nombre=nombre, apellido=apellido, email=email)
            else:
                errors.append("La fila del CSV no tiene suficientes datos")

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Archivo CSV cargado exitosamente")


class DescargarCSVClientes(View):
    def get(self, request):
        # genera los datos del archivo CSV
        clientes = Cliente.objects.all().values('documento', 'nombre', 'apellido', 'email')
        datos = list(clientes)

        # Verifica si hay datos para descargar
        if not datos:
            return HttpResponse("No hay clientes para descargar")

        # Construye el contenido del archivo CSV en una cadena
        csv_buffer = StringIO()
        fieldnames = ['documento', 'nombre', 'apellido', 'email']

        writer = csv.DictWriter(csv_buffer, fieldnames=fieldnames)
        writer.writeheader()

        for dato in datos:
            writer.writerow(dato)

        csv_content = csv_buffer.getvalue()

        # Construye la respuesta HTTP con el contenido del archivo CSV
        response = HttpResponse(csv_content, content_type='text/csv')

        # Configura el encabezado Content-Disposition para indicar la descarga
        response['Content-Disposition'] = 'attachment; filename="clientes.csv"'

        return response