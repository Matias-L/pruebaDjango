# pruebaDjango
Repositorio para introducirme en Django.

Basado en:
https://docs.docker.com/compose/django/

Para crear el directorio del proyecto y las aplicaciones, usar:
sudo docker-compose run web django-admin startproject projecto ./projecto/
sudo docker-compose run web django-admin startapp aplicacion ./aplicaciones

No olvidar de tener la carpeta "volumen" con sus subdirectorios "projecto" y "aplicaciones". "volumen" se mapea como "code" dentro del contenedor