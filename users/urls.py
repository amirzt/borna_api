from rest_framework.urls import path

from users import views

urlpatterns = [
    path('splash/', views.splash, name='splash'),
    path('grade/', views.get_grade, name='grade'),
    path('field/', views.get_field, name='field'),
    path('city/', views.get_city, name='city'),
    path('register/', views.register, name='register'),
    path('check_otp/', views.check_otp, name='check_otp'),

    path('add_student/', views.add_student, name='add_student'),
    path('get_student_info/', views.get_student_info, name='get_student_info'),
    path('update_student_info/', views.update_student_info, name='update_student_info'),
    path('get_home/', views.get_home, name='get_home'),
    path('get_universities/', views.get_universities, name='get_universities'),
    path('add_target/', views.add_target, name='add_target'),
    path('advisor_request/', views.advisor_request, name='advisor_request'),

]
