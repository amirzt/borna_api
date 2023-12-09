from rest_framework.urls import path

from curriculum import views

urlpatterns = [
    path('get_categories/', views.get_categories, name='get_categories'),
    path('add_curriculum/', views.add_curriculum, name='add_curriculum'),
    path('get_curriculum/', views.get_curriculum, name='get_curriculum'),
    path('delete_curriculum/', views.delete_curriculum, name='delete_curriculum'),
]
