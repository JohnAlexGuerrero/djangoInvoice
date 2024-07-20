from django.urls import path

from Category.views import categories_all, create_category, update_category

urlpatterns = [
    path('all/', categories_all, name='categories'),
    path('new/', create_category, name='category_new'),
    path('<int:pk>/edit/', update_category, name='category_edit'),

]
