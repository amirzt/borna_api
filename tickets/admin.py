from django.contrib import admin

# Register your models here.
from tickets.models import Ticket, Message, TicketCategory


@admin.register(TicketCategory)
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
    # list_filter = ('category',)
    # search_fields = ('name__startswith',)
    fields = ('ticket', 'content', 'sender')
