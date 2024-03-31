from rest_framework.urls import path

from league import views

urlpatterns = [
    path('get_league/', views.get_league)
]
