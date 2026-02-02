from django.shortcuts import render
from database import PRODUCTS
from .models import Product
# Create your views here.

def get_products(request):
    context = Product.objects.all()
    return render(request, 'products.html', {"product":context})

def detail(request, id):
    product_id = id
    product = Product.objects.get(id=product_id)

    

    return render(request, "detail.html", {"context":product})
    # buni ham yangiladim
