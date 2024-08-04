from django.contrib import admin

# Register your models here.
from field.models import FieldIntro, FieldAudio, FieldQuestion


@admin.register(FieldIntro)
class FieldIntroAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade',)
    # list_filter = ('grade', 'field')
    search_fields = ('name__startswith',)
    fields = ('name', 'grade', 'banner', 'button')


@admin.register(FieldAudio)
class FieldAudioAdmin(admin.ModelAdmin):
    list_display = ('intro', 'creator',)
    # list_filter = ('grade', 'field')
    # search_fields = ('name__startswith',)
    fields = ('intro', 'creator', 'file')


@admin.register(FieldQuestion)
class FieldAudioAdmin(admin.ModelAdmin):
    list_display = ('intro', 'title',)
    # list_filter = ('grade', 'field')
    # search_fields = ('name__startswith',)
    fields = ('intro', 'title', 'answer')
