from django.urls import path
from .views import ProductsView,UpdateProductView

urlpatterns = [
    path('',ProductsView.as_view(),name='products'),
    path('update/<int:id>/',UpdateProductView.as_view(),name='update'),
]
