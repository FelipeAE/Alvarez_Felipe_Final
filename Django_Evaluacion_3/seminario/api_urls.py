from django.urls import path
from seminario import api_views

urlpatterns = [
    path('datos_estudiante/',api_views.datos_estudiante,name="datos_estudiante"),
    path('api_inscritos_class/',api_views.InscritoList.as_view(),name="inscrito_list"),
    path('api_inscritos_class/<int:id>/',api_views.InscritoDetail.as_view(),name="inscrito_detail"),
    path('api_inscritos_function/',api_views.inscrito_list,name="inscrito_list"),
    path('api_inscritos_function/<int:id>/',api_views.inscrito_detail,name="inscrito_detail"),
    path('api_instituciones_class/',api_views.InstitucionList.as_view(),name="institucion_list"),
    path('api_instituciones_class/<int:id>/',api_views.InstitucionDetail.as_view(),name="institucion_detail"),
    path('api_instituciones_function/',api_views.institucion_list,name="institucion_list"),
    path('api_instituciones_function/<int:id>/',api_views.institucion_detail,name="institucion_detail"),
]