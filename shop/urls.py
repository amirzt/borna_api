from rest_framework.urls import path

from shop import views

urlpatterns = [
    path('get_zarinpal_plan/', views.get_zarinpal_plan, name='get_zarinpal_plan'),
    path('add_credit/', views.add_credit, name='add_credit'),
    path('send_request/', views.send_request, name='send_request'),
    path('verify/', views.verify, name='verify'),
    path('add_plan/', views.add_plan, name='add_plan'),

    # path('add_bazar_myket_order/', views.add_bazar_myket_order, name='add_bazar_myket_order'),
]