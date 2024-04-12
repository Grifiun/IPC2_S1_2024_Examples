DJANGO CONFIGURATION

Creaos Virtual environment
```bash
python -m venv myVenv
```

Ejecutamos el Venv en windows
```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\myVenv\Scripts\activate
```

o Ejecutamos el Venv en Linux
```bash
source myVenv/Scripts/activate
```
Instalamos Django
```bash
pip install django
```

creamos proyecto django
```bash
django-admin startproject nombre_del_proyecto
```

Ingresamos al proyecto creado y creamos una app
```bash
cd nombre_del_proyecto
django-admin startapp nombre_de_app
```

Migrate manage
```bash
python manage.py migrate
```
Creamos usuario administrador (datos ejemplo, configurar prudentemente)
```bash
python manage.py createsuperuser 
> Email Address: admin@admin.com
> Password: admin
> Password (Again): admin
```
Ejecutar Servidor
```bash
python manage.py runserver
```

-------------------------------------------------------------------
Create Templates in app folder
Settings.py
```py
Installed_apps [
	Add app
	'myApp'
]
```

urls.py (project)
agregar:
```py
	from django.urls import path, include
	path('', include("myApp.urls"))
```

urls.py (app)
```py
from . import views
from django.urls import path

urlpatterns = [
	path("", views.viewName, name="home"),
]
```

Views:
```py
from django.shortcuts import render

def viewName(request):
	context = {}
	return render(request, "myApp/home.html", context)
```


--------------------------------------------------------------------
Al usar formularios configurar:

{% csrf_token %}
