from rest_framework.urls import path

from league import views

urlpatterns = [
    path('get_league/', views.get_league),
    path('create_group/', views.create_group),
    path('delete_group/', views.delete_group),
    path('search_student/', views.search_student),
    path('add_member/', views.add_member),
    path('remove_user/', views.remove_user),
    path('get_groups/', views.get_groups),

]
