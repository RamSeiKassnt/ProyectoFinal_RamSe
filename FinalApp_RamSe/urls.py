from django.urls import path 

from FinalApp_RamSe.views import *

from django.contrib.auth.views import LogoutView

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    
    path('', inicio, name='Inicio'),
    path('autoFormulario',autoFormulario, name="AutoFormulario"),
    path('clienteFormulario',clienteFormulario, name="ClienteFormulario"),
    path('serviceFormulario',serviceFormulario, name="ServiceFormulario"),
    path('busquedaAuto', busquedaAuto, name="BusquedaAuto"),
    path('buscarAuto',buscarAuto, name="BuscarAuto"),
    path('busquedaCliente', busquedaCliente, name="BusquedaCliente"),
    path('busquedaService', busquedaService, name="BusquedaService"),
    path('buscarService',buscarService, name="BuscarService"),
    path('leerServices',leerServices, name="LeerServices"),
    path('leerAutos',leerAutos, name="LeerAutos"),
    path('leerClientes',leerClientes, name="LeerClientes"),
    path('eliminarAuto/<patenteAuto>', eliminarAuto, name="EliminarAuto"),
    path('eliminarCliente/<dni>', eliminarCliente, name="EliminarCliente"),
    path('eliminarService/<comprobanteNro>', eliminarService, name="EliminarService"),
    path('editarAuto/<patente>', editarAuto, name="EditarAuto"),
    path('editarCliente/<dni>', editarCliente, name="EditarCliente"),
    path('editarService/<comprobante>', editarService, name="EditarService"),
    path('login', login_request, name="Login"),
    path('register', register, name='Register'),
    path('logout', LogoutView.as_view(template_name='FinalApp_RamSe/logout.html'), name='Logout'),
    path('editarPerfil', editarPerfil, name="EditarPerfil"),
    path('aboutMe', aboutMe, name="AboutMe"),
    path('home', home, name="Home"),
    path('pages', pages, name="Pages"),
    path('verMas/<id>', verMas, name="VerMas"),
    path('comentarioFormulario', comentarioFormulario, name="ComentarioFormulario")

]

