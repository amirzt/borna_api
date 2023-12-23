from django.contrib import admin

# Register your models here.
from lessons.models import Lesson


@admin.register(Lesson)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'field')
    # list_filter = ('grade', 'field')
    search_fields = ('name__startswith',)
    fields = ('name', 'grade', 'field')
