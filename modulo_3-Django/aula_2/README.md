## Criando seu primeiro template

Os [Templates](https://docs.djangoproject.com/en/4.1/topics/templates/) são umas das bases de um framework. Ele servem como uma forma de gerar HTML dinamicamente. O django aceita múltiplos interpretadores de template, como o próprio Django Template Language (DTL), [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/), etc...  

Config default dos templates:

```python
# settings.py
# ...
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [], # diretórios customizados que possam ter templates
        "APP_DIRS": True, # buscar na árvore dos apps instalados
        "OPTIONS": { # configuraçoes especificas do backend
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
# ...
```
Usaremos o DTL por ter uma linguagem simples e que ja vem com configurações visuais.  

## Sobre o DTL:
### Variáveis
Renderizam o valor da variável nomeada naquele local, baseado no contexto que foi passado para o template. Então se eu tiver um no contexto:

```py
context = {"title": "Hello world"}
```

E no template eu tiver algo desse genero:

```jinja
{{ title }}, my name is Mateus!
```

O resultado será:
```htjinjaml
Hello world, my name is Mateus!
```

### Tags
Controlam a renderização do template atráves de lógicas arbitrátias. Podem serviir como condicionais e repetição. Utilizam a sintaxe `{% tag %}`.
[Built-in tags](https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#ref-templates-builtins-tags)

### Filtros
Transforma valores das variáveis e argumentos das tags.Ex:

```py
context = {"name": "mateus vALguEiro"}
```

```jinja
{{ name | title }}
```

O resultado será:
```html
Mateus Valgueiro
```

[Built-in filters](https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#ref-templates-builtins-filters)

