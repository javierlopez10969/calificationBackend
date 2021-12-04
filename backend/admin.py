from django.contrib import admin
from .models import Curso

# Agregar el curso al admin
admin.site.register(Curso)