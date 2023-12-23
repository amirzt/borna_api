from django.contrib import admin

# Register your models here.
from .models import CurriculumCategory


@admin.register(CurriculumCategory)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_filter = ('grade', 'field')
    search_fields = ('name__startswith',)
    fields = ('name',)
