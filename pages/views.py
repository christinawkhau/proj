from django.shortcuts import render
from products.models import Product
from products.models import Category

def index(request):
    return render(request, 'pages/index.html')

def categories(request):
    categories = Category.objects.all()
    return render(request, 'pages/categories.html', {'categories': categories})




