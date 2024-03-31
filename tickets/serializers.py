from rest_framework import serializers

from tickets.models import TicketCategory, Ticket, Message
from users.models import Student
from users.serializers import GetStudentInfoSerializer


class TicketCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketCategory
        fields = ('id', 'name')


class AddTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['category']

    def save(self, **kwargs):
        ticket = Ticket(category=self.validated_data['category'],
                        student=Student.objects.get(user=self.context['user']))
        ticket.save()

        message = Message(ticket=ticket,
                          content=self.context.get('content'))
        message.save()
        return ticket


class GetTicketSerializer(serializers.ModelSerializer):
    student = GetStudentInfoSerializer()
    last_message = serializers.SerializerMethodField('get_last_message')

    @staticmethod
    def get_last_message(self):
        messages = Message.objects.filter(ticket=self).order_by('created_at').last()
        return GetMessageSerializer(messages).data

    class Meta:
        model = Ticket
        fields = ('id', 'category', 'created_at', 'state', 'student', 'last_message')


class GetMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'content', 'created_at', 'sender')


class AddMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['content', 'sender', 'ticket']

    def save(self, **kwargs):
        message = Message(ticket=self.validated_data['ticket'],
                          content=self.validated_data['content'],
                          sender=self.validated_data['sender'])
        message.save()
        return message
