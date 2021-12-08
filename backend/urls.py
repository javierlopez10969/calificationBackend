from django.urls import path , include 
from .views import curso_list,curso_detalle

urlpatterns = [
    path('cursos/', curso_list),
    path('curso/<int:pk>/', curso_detalle)
]
