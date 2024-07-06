from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
import json

from Product.models import Product
from Product.forms import ProductNewForm

# Create your views here.

#list all brands
def list_brands(request):
    brands = Product.objects.all().values('id','brand')
    print()
    return JsonResponse({
        "brands":[
            {
                "id": x['id'],
                "name":x['brand']
            }
            for x in brands
        ]
    })

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
@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        product = Product(
            description=data['description'],
            codebar=data['codebar'],
            brand=data['brand'],
            stock=data['qty'],
            unit=data['unit'],
            cost=data['cost'],
            price=data['price']
        )
        if product:
            product.save()
            response_data = {
                'message': 'Producto creado con éxito.',
            }
            return JsonResponse(response_data)   
        
    return JsonResponse({'message':'Invalid request method. Use POST to create a product.'})
         

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