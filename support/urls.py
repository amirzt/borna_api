from rest_framework.urls import path

from support import views

urlpatterns = [
    path('get_questions/', views.get_questions, name='get_questions'),
]
