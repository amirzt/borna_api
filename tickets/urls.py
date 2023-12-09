from rest_framework.urls import path

from tickets import views

urlpatterns = [
    path('categories/', views.get_categories, name='get_categories'),
    path('add_ticket/', views.add_ticket, name='add_ticket'),
    path('get_tickets/', views.get_tickets, name='get_tickets'),
    path('get_messages/', views.get_messages, name='get_messages'),
    path('add_message/', views.add_message, name='add_message'),
]
