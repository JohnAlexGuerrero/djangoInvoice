from django.urls import path

from Product.views import list_products, create_product, product_detail, filter_products

urlpatterns = [
    #GET api/v1/inventario/all
    path('all/', list_products, name='products'),
    #POST api/v1/inventario/new
    path('new/', create_product, name='product_new'),
    #GET api/v1/inventario/item/:slug
    path('item/<slug:slug>', product_detail, name='product_detail'),
    #UPDATE api/v1/inventario/item/:slug/active
    # path('item/<slug:slug>/active', name='product_active'),
    #UPDATE api/v1/inventario/item/:slug/stock
    # path('item/<slug:slug>/add-stock', name='product_add_stock'),
    #POST: api/v1/search
    path('search', filter_products, name='search'),
]
