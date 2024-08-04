from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/content/', include('content.urls')),
    path('api/curriculum/', include('curriculum.urls')),
    path('api/lessons/', include('lessons.urls')),
    path('api/shop/', include('shop.urls')),
    path('api/support/', include('support.urls')),
    path('api/tickets/', include('tickets.urls')),
    path('api/users/', include('users.urls')),
    path('api/league/', include('league.urls')),
    path('api/todo/', include('todo.urls')),
    path('api/field/', include('field.urls')),

]
