from django.urls import path
from .views import login
from .views_warehouse import warehouse_create, warehouse_list, warehouse_edit, warehouse_delete

urlpatterns = [
    path('', login, name='login'),
    path('warehouses/', warehouse_list, name='warehouse_list'),
    path('warehouses/new/', warehouse_create, name='warehouse_create'),
    path('warehouses/edit/<int:pk>/', warehouse_edit, name='warehouse_edit'),
    path('warehouses/delete/<int:pk>/', warehouse_delete, name='warehouse_delete'),
]
