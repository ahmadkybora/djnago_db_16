from django.urls import path
from .views import index, show, store, update

urlpatterns = [
    path('', index),
    path('<int:pk>/', show),
    path('store/', store),
    path('update/<int:pk>/', update)
]