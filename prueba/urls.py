"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse
from rest_framework import routers
from factura import views
from rest_framework.authtoken import views as token
from factura.views import RegistroUsuarioAPIView, IniciarSesionAPIView, DescargarCSVClientes, CargarCSVClientes



router = routers.DefaultRouter()
router.register(r'clientes', views.ClienteViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'facturas', views.FacturaViewSet)
router.register(r'productosFactura', views.ProductoFacturaViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api', include('rest_framework.urls', namespace='rest_framework')),
    path('auth-token', token.obtain_auth_token),
    path('clientes', views.ClienteViewSet.as_view({'get': 'list', 'post': 'create'}), name='cliente-list'),
    path('clientes/<int:pk>', views.ClienteViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='cliente-detail'),
    path('facturas', views.FacturaViewSet.as_view({'get': 'list', 'post': 'create'}), name='factura-list'),
    path('facturas/<int:pk>', views.FacturaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='factura-detail'),
    path('productos/', views.ProductoViewSet.as_view({'get': 'list', 'post': 'create'}), name='producto-list'),
    path('productos/<int:pk>', views.ProductoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='producto-detail'),
    path('productosFactura', views.ProductoFacturaViewSet.as_view({'get': 'list', 'post': 'create'}), name='productofactura-list'),
    path('productosFactura/<int:pk>', views.ProductoFacturaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='productofactura-detail'),
    path('registro-usuario', views.RegistroUsuarioAPIView.as_view(), name='registro-usuario'),
    path('iniciar-sesion', views.IniciarSesionAPIView.as_view(), name='iniciar-sesion'),
    path('cargar-csv-clientes', views.CargarCSVClientes.as_view(), name='cargar-csv-clientes'),
    path('descargar-csv', views.DescargarCSVClientes.as_view(), name='descargar-csv'),    
    
]

