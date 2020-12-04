from django.urls import path
from .views import  ProductListView, ProductDetailView

urlpatterns=[
    path("app/products", ProductListView.as_view()),
    path("app/products/<int:pid>", ProductDetailView.as_view())
]