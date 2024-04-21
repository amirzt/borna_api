from rest_framework.urls import path

from content import views

urlpatterns = [
    path('get_content_categories/', views.get_content_categories, name='get_content_categories'),
    path('get_content/', views.get_content, name='get_content'),
    path('get_exam/', views.get_exam, name='get_exam'),
    path('add_content_access/', views.add_content_access, name='add_content_access'),

]
