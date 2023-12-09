from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'price', 'status', 'date',)
    list_filter = ('status', 'date',)
    fields = ('user', 'date', 'price', 'status', 'payment_method', 'tracking_code', 'description', 'gateway')
