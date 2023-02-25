## Comandos iniciais

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

## Adicionando um model
```bash
# Cria as migraçoes
$ python manage.py makemigrations store

# Verificar o comando sql que foi gerado
$ python manage.py sqlmigrate store 0001

# Roda a migration
$ python manage.py migrate
```
## FAQ
### CharField vs TextField
A mesma coisa que varchar vs text. No caso do CharField vc precisa passar o limite maximo de tamanho, enquanto o TextField nao precisa
