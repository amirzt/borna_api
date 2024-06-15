from django.contrib import admin

# Register your models here.
from support.models import FrequentlyAskedQuestion


@admin.register(FrequentlyAskedQuestion)
class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'type')
    search_fields = ('question__startswith',)
    fields = ('question', 'answer', 'type')