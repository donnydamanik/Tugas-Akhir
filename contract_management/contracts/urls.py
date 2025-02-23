from django.urls import path
from . import views  # Impor views dari aplikasi saat ini

urlpatterns = [
    path('', views.contract_list, name='contract_list'),
    path('create/', views.contract_create, name='contract_create'),
    path('<int:pk>/edit/', views.contract_update, name='contract_update'),
    path('<int:pk>/delete/', views.contract_delete, name='contract_delete'),
]
