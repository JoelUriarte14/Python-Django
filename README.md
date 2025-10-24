Proyecto de Encuestas (Tutorial de Django)

Este es el proyecto de aplicación de encuestas ("Polls app") construido siguiendo el tutorial oficial de Django (versión 5.x).

Es una aplicación web full-stack que demuestra las características fundamentales de Django. Permite a los usuarios ver preguntas, votar en ellas, y proporciona un panel de administración (CMS) para que el administrador gestione todo el contenido.

¿Cómo ejecutar este proyecto?

Si descargaste este código, sigue estos pasos para ponerlo en marcha:

1. Prerrequisitos

Tener Python 3.10 o superior instalado.

2. Configuración del Entorno

Clona o descarga este repositorio.

Abre una terminal en la carpeta raíz del proyecto (donde está manage.py).

Crea un entorno virtual (una "caja" para tus librerías):

python -m venv venv


Activa el entorno virtual:

En Windows (PowerShell):

.\venv\Scripts\activate


En macOS/Linux:

source venv/bin/activate


(Deberías ver un (venv) al inicio de tu terminal).

Instala las dependencias (en este caso, solo Django):

pip install django


3. Configuración de la Base de Datos

Aplica las migraciones para crear las tablas en la base de datos (db.sqlite3):

python manage.py migrate


Crea un superusuario para poder acceder al panel de administración:

python manage.py createsuperuser


(Te pedirá un nombre de usuario, email y contraseña. ¡No olvides la contraseña!)

4. ¡Arranca el servidor!

python manage.py runserver


El proyecto estará corriendo en http://127.0.0.1:8000/.

Puntos Clave de la Aplicación (URLs para visitar)

Para entender la aplicación, tienes que entrar a dos secciones principales: el sitio público (lo que ve el usuario) y el panel de administración (lo que ves tú).

1. El Sitio Público

Estas son las páginas que ve cualquier visitante.

Página Principal (Índice):

URL: http://127.0.0.1:8000/polls/

Qué hace: Muestra una lista de las últimas 5 preguntas publicadas.

Página de Detalle (Votación):

URL (Ejemplo): http://127.0.0.1:8000/polls/1/

Qué hace: Muestra el texto de una pregunta específica (en este caso, la ID 1) y un formulario con botones de radio para votar.

Página de Resultados:

URL (Ejemplo): http://127.0.0.1:8000/polls/1/results/

Qué hace: Muestra los resultados de la votación para la pregunta 1. A esta página se te redirige después de votar.

2. El Panel de Administración (CMS)

Esta es la zona privada para gestionar el contenido.

Página de Login del Admin:

URL: http://127.0.0.1:8000/admin/

Qué hace: Te pide el nombre de usuario y contraseña del superuser que creaste en el paso 3 de la configuración.

Gestión de Contenido:

Una vez dentro del admin, podrás ver la sección "POLLS".

Desde ahí puedes Añadir, Modificar y Borrar "Questions" (Preguntas) y "Choices" (Opciones).

Cualquier cambio que hagas aquí se reflejará inmediatamente en el sitio público.

Estructura de Archivos Clave

mysite/settings.py: El archivo de configuración principal. Aquí registramos la app polls en INSTALLED_APPS.

mysite/urls.py: El "enrutador" principal. Le dice a Django que envíe las URLs /polls/ a la app polls y /admin/ al admin.

polls/models.py: Los "planos" de la base de datos. Aquí definimos las clases Question y Choice.

polls/views.py: El "cerebro" de la app. Contiene la lógica (las Clases IndexView, DetailView, etc.) que decide qué datos mostrar en cada página.

polls/admin.py: Configura cómo se ven los modelos Question y Choice en el panel de admin (por ejemplo, añadiendo las opciones "inline").

polls/templates/polls/: La carpeta que contiene todos los archivos HTML que ve el usuario (index.html, detail.html, results.html).

polls/static/polls/: La carpeta que contiene los archivos estáticos (como style.css).

polls/tests.py: Contiene las pruebas automáticas para asegurar que la app funcione correctamente.