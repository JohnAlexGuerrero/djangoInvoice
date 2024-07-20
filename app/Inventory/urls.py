from django.urls import path
from Inventory.views import HomeView

urlpatterns = [
    #GET inventory
    path('', HomeView.as_view(), name='inventory'),
    path('category/<slug:slug>/', HomeView.as_view(), name='by_category'),
]
