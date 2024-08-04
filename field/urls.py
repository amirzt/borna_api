from rest_framework.urls import path
from . import views

urlpatterns = [
    path('get_intro/', views.get_intro)
]
