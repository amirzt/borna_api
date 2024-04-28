from django.contrib import admin

# Register your models here.
from content.models import ContentCategory, Content, Exam, ContentAccess


@admin.register(ContentCategory)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_filter = ('app_type', 'version')
    search_fields = ('name__startswith',)
    fields = ('name', 'description', 'image', 'is_special', 'is_free', 'price', 'is_clone')


@admin.register(Content)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('category', 'type', 'orientation')
    search_fields = ('title__startswith',)
    fields = ('category', 'type', 'orientation', 'title', 'subtitle', 'description', 'preview_image', 'content',)


@admin.register(Exam)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('lesson', 'type')
    search_fields = ('title__startswith',)
    fields = ('lesson', 'title', 'subtitle', 'file', 'type')


@admin.register(ContentAccess)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('student', 'category', 'created_at')
    list_filter = ('category',)
    # search_fields = ('title__startswith',)
    fields = ('student', 'category',)
