from django.contrib import admin

# Register your models here.
from content.models import Category
from tickets.models import Ticket, Message


@admin.register(Category)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_filter = ('grade', 'field')
    search_fields = ('name__startswith',)
    fields = ('name',)


@admin.register(Ticket)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('student',)
    list_filter = ('category',)
    # search_fields = ('name__startswith',)
    fields = ('category', 'student', 'state')


@admin.register(Message)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'created_at')
    list_filter = ('category',)
    # search_fields = ('name__startswith',)
    fields = ('ticket', 'content', 'sender')
