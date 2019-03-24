# pruebaDjango
Repositorio para introducirme en Django.

Basado en:
https://docs.docker.com/compose/django/
https://docs.djangoproject.com/es/2.1/intro/tutorial01/

Para crear el directorio del proyecto y las aplicaciones, usar:
sudo docker-compose run web django-admin startproject projecto ./projecto/
sudo docker-compose run web django-admin startapp aplicacion ./projecto/calculadora

No olvidar de tener la carpeta "volumen" con sus subdirectorios "projecto" y "calculadora". "volumen" se mapea como "code" dentro del contenedor
Luego de configurar la base de datos en "settings.py", y haber creado la vista y URL siguiendo el tutorial, hacer docker-compose up. En otra terminal, entrar al bash del
contenedor web, y aplicar python manage.py migrate

Guía de tres pasos para hacer cambios de modelo:
Cambie sus modelos (en models.py).
Ejecute el comando python manage.py makemigrations para crear migraciones para esos cambios
Ejecute el comando python manage.py migrate para aplicar esos cambios a la base de datos.

