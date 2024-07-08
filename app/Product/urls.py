from django.urls import path

from Product.views import list_products, create_product, product_detail, filter_products, list_brands, update_product
from Product.views import HomeView

urlpatterns = [
    #GET inventory
    path('', HomeView.as_view(), name='inventory'),
    #GET api/v1/inventario/all
    path('all/', list_products, name='products'),
    #POST api/v1/inventory/new
    path('new/', create_product, name='product_new'),
    #GET api/v1/inventory/item/:pk
    path('item/<int:pk>', product_detail, name='product_detail'),
    #UPDATE api/v1/inventory/item/:pk/edit
    path('item/<int:pk>/edit', update_product, name='product_edit'),
    #UPDATE api/v1/inventario/item/:slug/active
    # path('item/<slug:slug>/active', name='product_active'),
    #UPDATE api/v1/inventario/item/:slug/stock
    # path('item/<slug:slug>/add-stock', name='product_add_stock'),
    #POST: api/v1/inventory/search
    path('search', filter_products, name='search'),
    #GET: api/v1/inventory/brands
    path('brands/', list_brands, name="brands")
]
