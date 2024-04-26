from . import views
from django.urls import path

urlpatterns = [
	path("", views.index),
    path("formulario", views.formulario),
    path("formulario_nombre", views.formulario_nombre),
    path("procesar_formulario", views.procesar_formulario),
    path("procesar_formulario_nombre", views.procesar_formulario_nombre),
    path("pagina_hija_1", views.pagina_hija_1),
    path("pagina_hija_2", views.pagina_hija_2),
]

