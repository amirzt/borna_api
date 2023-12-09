from rest_framework.urls import path

from lessons import views

urlpatterns = [
    path('get_lessons/', views.get_lessons, name='get_lessons'),
]