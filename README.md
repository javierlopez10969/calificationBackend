# Tutorial ed django web-app

## Requisitos

Django > 2.1

Python > 3.7

python3 -m venv env
source env/bin/activate

### Primer paso crear el proyecto

django-admin startproject backend_califications_system
django-admin startproject califications-rest

Migrar la base de datos.

### `python manage.py migrate`

### Levantar el proyecto 

### `python manage.py runserver`

### Crear una nueva application

Django permite tener multiples aplicaciones para un solo proyecto, para ello crearemos una nueva app mediante el comando :

### `python manage.py startapp backend`

### Creando página para administrador

Para ello crearemos a un usuario administrador con : 

### `python manage.py migrate`
### `python manage.py makemigrations`
### `python manage.py createsuperuser`

### Creando modelos para la base de datos
 
En la aplicación creada añadiremos nuestros modelos en el módulos models.py. Además ens etting.py añadiremos las apps creadas.

Con los modelos los migraremos mediante 

### `python manage.py migrate`
### `python manage.py makemigrations`

Con estos modelos creados los agregaremos en modulo admin.py :

from .models import Curso
admin.site.register(Curso)

### Crear una clase serializadora

Esta clase nos permitira formatear nuestros modelos a un formato json. Para ello crearemos un modulo serializer en la aplicación. serializer.py. importaremos nuestros modelos y crearemos las distintas clases que serializaran nuestros modelos. En esta sección crearemos el crud para los modelos.

Para probar que funciona lo que se ha hecho puede ingresar a la consola del proyecto :
 
### `python manage.py shell`

Comando que nos traduce la base de datos a sql

### `python manage.py sqlmigrate blog`

En consola :

from backend.models import Curso
from backend.serializer import CursoSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
a = Curso(nombre='Algebra I sección Nelson',estado= True , promedio = 1.0)
a.save()
serializer= CursoSerializer(a)
serializer.data
content = JSONRenderer().render(serializer.data)
serializer= CursoSerializer(Curso.objects.all(),many=True)
serializer.data

### Crear una clase como template

En el modulo serializer.py crear una clase Meta con las variables de los modelos :

`class CursoSerializer(serializers.ModelSerializer):`
`class Meta:`
`    model = Curso`
`    fields = ['id','nombre','estado','promedio'] `

En consola :

serializer = CursoSerializer()
print(repr(serializer))

### Vistas basadas en apis













### Modificando las vistas

Abriremos el modulo views.py de la carpeta que acabamos de crear. En este modulo se crearan las logicas necesarias para todas las vistas y rutas que necesitemos para nuestra aplicación.

A continuación creamos un modulo llamado urls.py e importamos path y las vistas que acabamos de crear en views.py.

Ahora configuramos el urls.py del proyecto general  donde incluiremos las vistas y rutas recien creadas.


### Creando vistas para el backend en templates






