from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q

from Product.models import Product
from Product.forms import ProductNewForm

# Create your views here.

#list all products
def list_products(request):
    items = Product.objects.all()
    
    return JsonResponse({
        "items":[
            {
                'id': item.id,
                'description': item.description,
                'slug': item.slug,
                'brand': item.brand,
                'codebar': item.codebar,
                'stock': item.stock,
                'und': item.unit,
                'price': item.price
            }
            for item in items
        ]    
    })

#create new product
def create_product(request):
    if request.method == 'POST':
        form = ProductNewForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message':'Producto creado con exito.'
            })

#GET: details product
def product_detail(request):
    item = Product.objects.get(slug=request.GET.get('slug'))

    return JsonResponse({
        [
            {
                'id': item.id,
                'description': item.description,
                'slug': item.slug,
                'brand': item.brand,
                'codebar': item.codebar,
                'stock': item.stock,
                'und': item.und,
                'price': item.price
            }
            
        ]
    })

#GET: filter products by description
def filter_products(request):
    
    if request.GET.get('q'):
        items = Product.objects.filter(
            Q(description__icontains=request.GET.get('q'))
        )
        print(items)
        
        return JsonResponse({
            "items":[
                {
                    'id': item.id,
                    'description': item.description,
                    'slug': item.slug,
                    'brand': item.brand,
                    'codebar': item.codebar,
                    'stock': item.stock,
                    'unit': item.unit,
                    'price': item.price
                }
                for item in items
            ]    
        })