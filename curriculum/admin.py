from django.contrib import admin

# Register your models here.
from content.models import Category


@admin.register(Category)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_filter = ('grade', 'field')
    search_fields = ('name__startswith',)
    fields = ('name',)
