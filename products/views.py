from django.shortcuts import render, get_object_or_404
from .models import Category
from .models import Product 
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from . choices import category_choices, brand_choices, price_choices
from django.db.models import Q
# Create your views here.


def products(request):
    products=Product.objects.filter(is_active=True)
    
    paginator=Paginator(products,3) 
    page=request.GET.get('page')
    paged_products=paginator.get_page(page) 
    context ={"products":paged_products} 
    return render(request, 'products/products.html', context)

def product(request, product_id):
    product=get_object_or_404(Product, pk=product_id) 
    context={"product":product}
    return render(request, 'products/product.html', context)


def search(request):
    queryset_list=Product.objects.order_by('-price')
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            queryset_list=queryset_list.filter(Q(description__icontains=keywords) | Q(category__icontains=keywords) | Q(name__icontains=keywords) | Q(brand__icontains=keywords))

    if 'category' in request.GET:
        category =request.GET['category']
        if category:
            queryset_list=queryset_list.filter(category__iexact=category)

    if 'brand' in request.GET:
        brand =request.GET['brand']
        if brand:
            queryset_list=queryset_list.filter(brand__iexact=brand)

    if 'price' in request.GET:
        price =request.GET['price']
        if price: 
            queryset_list=queryset_list.filter(price__lte=price)        
    
    paginator=Paginator(queryset_list,3) 
    page=request.GET.get('page')
    paged_products=paginator.get_page(page) 
   
    context={"products":paged_products,
            "category_choices":category_choices,
            "brand_choices":brand_choices,
            "price_choices":price_choices,        
            "values":request.GET}    
    return render(request, 'products/search.html', context)


# def categories(request):
#     categories = Category.objects.all()
#     return render(request, 'pages/categories.html', {'categories': categories})

# def products(request, category_id):
#     category = get_object_or_404(Category, id=category_id)
#     products = Product.objects.filter(category=category)
#     return render(request, 'products/products_a.html', {'category': category, 'products': products})

# def product(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     return render(request, 'products/product_a.html', {'product': product})


