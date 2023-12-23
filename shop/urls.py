from rest_framework.urls import path

from shop import views

urlpatterns = [
    path('get_zarinpal_plan/', views.get_zarinpal_plan, name='get_zarinpal_plan'),
    path('add_bazar_myket_order/', views.add_bazar_myket_order, name='add_bazar_myket_order'),
]