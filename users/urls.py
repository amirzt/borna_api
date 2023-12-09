from rest_framework.urls import path

from users import views

urlpatterns = [
    path('grade/', views.get_grade, name='grade'),
    path('field/', views.get_field, name='field'),
    path('city/', views.get_city, name='city'),
    path('register/', views.register, name='register'),
    path('get_student_info/', views.get_student_info, name='get_student_info'),
    path('update_student_info/', views.update_student_info, name='update_student_info'),
]
