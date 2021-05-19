from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name = "About"),
    path('products/<int:my_id>', views.product_view, name="ProductView"),
    path('viewall/<str:my_category>', views.viewall, name="ViewAll")
]




