from django.contrib import admin
from . import models

# Register your models here.
from .models import Plan, ZarinpalMerchantCode


@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'price', 'status', 'date',)
    list_filter = ('status', 'date',)
    fields = ('user', 'price', 'status', 'payment_method', 'tracking_code', 'description', 'gateway')


@admin.register(Plan)
class FontAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_available', 'duration',)
    # list_filter = ('category', 'is_done', 'date',)
    search_fields = ('title__startswith',)
    fields = ('title', 'price', 'is_available', 'duration', 'description', 'bazar_myket',)


admin.site.register(ZarinpalMerchantCode)