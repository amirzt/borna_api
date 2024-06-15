from django.contrib import admin

# Register your models here.
from content.models import ContentCategory, Content, Exam, ContentAccess, Chapter, Comment


@admin.register(ContentCategory)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_filter = ('app_type', 'version')
    search_fields = ('name__startswith',)
    fields = ('name', 'description', 'image', 'is_special', 'is_free', 'price', 'is_clone',
              'preview_video', 'preview_image', 'preview_description', 'discount', 'discount_expire_date')


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title',)
    # list_filter = ('app_type', 'version')
    search_fields = ('title__startswith',)
    fields = ('title', 'category', 'description',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('category', 'student')
    # list_filter = ('app_type', 'version')
    search_fields = ('title__startswith',)
    fields = ('student', 'category', 'content', 'file')


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
