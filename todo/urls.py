from rest_framework.urls import path

from todo import views

urlpatterns = [
    path('add_task/', views.add_task, name='add_task'),
    path('get_tasks/', views.get_tasks, name='get_tasks'),
    path('delete_tasks/', views.delete_tasks, name='delete_tasks'),
    path('update_task/', views.update_task, name='update_task'),
]
