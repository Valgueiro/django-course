```bash
# Configurando o PYENV após instalaçao
$ pyenv virtualenv 3.10 curso-django
$ pyenv activate curso-django

# =======
# Instala django e cria um novo projeto
$ pip install "Django==4.1"
$ django-admin startproject project_curso_django
# =======
# Roda pela primeira vez para ver a pagina inicial
$ python manage.py runserver

# =====
# Roda as migrations
$ python manage.py migrate

# =====
# cria primeiro app
$ python manage.py startapp store
```
