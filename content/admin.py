from django.contrib import admin

# Register your models here.
from content.models import Category, Content, Exam


@admin.register(Category)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_filter = ('app_type', 'version')
    search_fields = ('name__startswith',)
    fields = ('name', 'description', 'type', 'image',)


@admin.register(Content)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('category',)
    search_fields = ('title__startswith',)
    fields = ('category', 'title', 'subtitle', 'description', 'preview_image', 'content', )


@admin.register(Exam)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('grade', 'field')
    search_fields = ('title__startswith',)
    fields = ('grade', 'field', 'title', 'subtitle', 'file', )
