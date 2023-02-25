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

## Setup Admin
```bash
# Cria um superuser
$ python manage.py createsuperuser

# Verificar o comando sql que foi gerado
$ python manage.py sqlmigrate store 0001

# Roda a migration
$ python manage.py migrate
```

## QuerySet
```bash
$ python manage.py shell
```
``` python
>> from store.models import Product
# listar
>> Product.objets.all()
>> Product.objects.filter(name="")
>> Product.objects.filter(name="").filter(price="")
>> Product.objects.filter(name__startswith="P")
>> Product.objects.order_by("name")
>> Product.objects.order_by("name")
# criar novo
>> product = Product(name="Piloto", description="Piloto muito bom :+1:", price=3.15)
>> product.save()
# ou
>> Product.objects.create(...attrs)
# update
>> product = Product.objects.get(name="Piloto")
>> product.name = "Piloto Preto"
>> product.save()
## delete
>> Product.objects.filter(name__startswith="P").delete()
```
## FAQ
### CharField vs TextField
A mesma coisa que varchar vs text. No caso do CharField vc precisa passar o limite maximo de tamanho, enquanto o TextField nao precisa

