from django.db import models

class UnavailableManager(models.Manager):
    def get_queryset(self):
        return super(UnavailableManager, self).get_queryset().filter(available=False)

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    
    # auto generated
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager() # default
    unavailable = UnavailableManager() # nosso manager
    def __str__(self):
        return f"{self.name} -> R$ {self.price}"

