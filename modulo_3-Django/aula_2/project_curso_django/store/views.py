from django.shortcuts import render
from .models import Product

# Create your views here.

def hello(request):
    return render(request, "index.html")


def product_list(request):
    products = Product.objects.all()
    return render(request,
                "product/list.html",
                { "products": products })
