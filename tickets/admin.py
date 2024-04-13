from django.contrib import admin

# Register your models here.
from tickets.models import Ticket, Message, TicketCategory


@admin.register(TicketCategory)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_filter = ('grade', 'field')
    search_fields = ('name__startswith',)
    fields = ('name',)


# @admin.register(Message)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('ticket', 'created_at')
#     # list_filter = ('category',)
#     # search_fields = ('name__startswith',)
#     fields = ('ticket', 'content', 'sender')

class MessageInline(admin.TabularInline):
    model = Message
    extra = 0


@admin.register(Ticket)
class CustomUserAdmin(admin.ModelAdmin):
    inlines = [MessageInline]
    list_display = ('student', 'last_message_sender', 'last_message_content')
    list_filter = ('category', 'state')
    # search_fields = ('name__startswith',)
    fields = ('category', 'student', 'state')

    def last_message_content(self, obj):
        last_message = Message.objects.filter(ticket=obj).last()
        if last_message:
            return last_message.content
        else:
            return "No messages"

    last_message_content.short_description = 'Last Message Content'

    def last_message_sender(self, obj):
        last_message = Message.objects.filter(ticket=obj).last()
        if last_message:
            return last_message.sender
        else:
            return "No messages"

    last_message_sender.short_description = 'Last Message Sender'
