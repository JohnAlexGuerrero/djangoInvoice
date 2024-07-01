from django.urls import path

from Invoicing.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='invoice'),
]
