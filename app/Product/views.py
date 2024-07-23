from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
import decimal

from Product.models import Product
from Category.models import Category

from Product.forms import ProductNewForm

# Create your views here.
#GET: filter products by category and search item with input
def search_item_in_category(request, *args, **kwargs):
    if kwargs['slug']:
        items = Product.objects.filter(category__slug=kwargs['slug'])
        items = items.filter(Q(description__icontains=request.GET.get('q')))

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
    
#GET: filter products by category
def filter_product_by_category(request, *args, **kwargs):
    if kwargs['slug']:
        items = Product.objects.filter(category__slug=kwargs['slug'])

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

#patch product
@csrf_protect
def update_product(request, *args, **kwargs):
    if request.method == 'PATCH':
        data = json.loads(request.body.decode('utf-8'))
        product = Product.objects.get(id=kwargs['pk'])
        
        if product:
            product.description = data['description']
            product.codebar = data['codebar']
            product.brand = data['brand']
            product.stock = data['stock']
            product.unit = data['unit']
            product.cost = decimal.Decimal(data['cost'])
            product.price = decimal.Decimal(data['price'])
            product.category = data['category']
            product.save()
 
            return JsonResponse({
                'message':f'{product.description} fue actualizado con exito.'
            })
    return JsonResponse({
        'message':'no fue posible la actualización.'
    })
    
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
    items = Product.objects.all().order_by('-id')
    
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
                'price': item.price,
            }
            for item in items
        ]
    })

#create new product
@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        category = Category.objects.get(id=data['category'])
        
        product = Product(
            description=data['description'],
            codebar=data['codebar'],
            brand=data['brand'],
            stock=data['qty'],
            unit=data['unit'],
            cost=data['cost'],
            price=data['price'],
            category= category
        )
        if product:
            product.save()
            response_data = {
                'message': 'Producto creado con éxito.',
            }
            return JsonResponse(response_data)   
        
    return JsonResponse({'message':'Invalid request method. Use POST to create a product.'})
         

#GET: details product
def product_detail(request, *args, **kwargs):
    item = Product.objects.get(id=kwargs['pk'])

    return JsonResponse({
        "item":[
            {
                'id': item.id,
                'description': item.description,
                'slug': item.slug,
                'brand': item.brand,
                'codebar': item.codebar,
                'stock': item.stock,
                'unit': item.unit,
                'price': item.price,
                'cost': item.cost
            }
            
        ]
    })

#GET: filter products by description
def filter_products(request):
    if request.GET.get('q'):
        items = Product.objects.filter(
            Q(description__icontains=request.GET.get('q'))
        )
        
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