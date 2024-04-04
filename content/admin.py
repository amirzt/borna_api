from django.contrib import admin

# Register your models here.
from content.models import ContentCategory, Content, Exam


@admin.register(ContentCategory)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_filter = ('app_type', 'version')
    search_fields = ('name__startswith',)
    fields = ('name', 'description', 'image', 'is_special')


@admin.register(Content)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('category',)
    search_fields = ('title__startswith',)
    fields = ('category', 'type', 'title', 'subtitle', 'description', 'preview_image', 'content', )


@admin.register(Exam)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('lesson', 'type')
    search_fields = ('title__startswith',)
    fields = ('lesson', 'title', 'subtitle', 'file', 'type')
