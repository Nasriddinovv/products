from django.shortcuts import render
from database import PRODUCTS
# Create your views here.

def get_products(request):
    context = PRODUCTS
    return render(request, 'products.html', context)

def detail(request, id):
    
    prodcut_id = id
    context = {}
    
    for cat in PRODUCTS["categories"]:
        for i in PRODUCTS["categories"][cat]:
            if i['id'] == prodcut_id:
                context["product"] = i 
                print(i)
    

    return render(request, "detail.html", context)