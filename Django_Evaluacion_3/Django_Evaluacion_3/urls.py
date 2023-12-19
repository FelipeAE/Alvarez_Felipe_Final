"""
URL configuration for Django_Evaluacion_3 project.

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
from django.urls import path,include
from seminario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("inscritos/",views.lista_inscritos,name="lista_inscritos"),
    path("inscritos/agregar/",views.agregar_inscrito,name="agregar_inscrito"),
    path("inscritos/editar/<int:id>/",views.editar_inscrito,name="editar_inscrito"),
    path("inscritos/eliminar/<int:id>/",views.eliminar_inscrito,name="eliminar_inscrito"),
    path("instituciones/",views.lista_instituciones,name="lista_instituciones"),
    path("instituciones/agregar/",views.agregar_institucion,name="agregar_institucion"),
    path("instituciones/editar/<int:id>/",views.editar_institucion,name="editar_institucion"),
    path("instituciones/eliminar/<int:id>/",views.eliminar_institucion,name="eliminar_institucion"),
    path("api/",include("seminario.api_urls")),
    path('seminario/',include('seminario.urls')),
]
