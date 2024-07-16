from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from Category.models import Category

# Create your views here.
def categories_all(request):
    categories = Category.objects.all().order_by('description')
    
    return JsonResponse({
        "data": [
            {
                "id": category.id,
                "description": category.description
            }
            for category in categories
        ]
    })

@csrf_exempt
def create_category(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        category = Category(description=data['description'])
        
        if category:
            category.save()
            response_data = {
                'method': request.method,
                'Content-Type': request.content_type,
                'message': 'La categoria fue creada con éxito.',
            }
                        
            return JsonResponse(response_data)
    return JsonResponse({'message':'Invalid request method. Use POST to create a product.'})

@csrf_exempt
def update_category(request, *args, **kwargs):
    if request.method == 'PATCH':
        data = json.loads(request.body.decode('utf-8'))
        category = Category.objects.get(id=kwargs['pk'])
        
        if category:
            category.description = data['description']
            category.save()
            
            return JsonResponse({
                'message':f'{category.description} fue actualizado con exito.'
            })
    return JsonResponse({
        'message':'no fue posible la actualización.'
    })