from django.db import models

# Create your models here.
from users.models import Student


class TicketCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    class State(models.TextChoices):
        CLOSED = 'closed', 'Closed'
        IN_PROGRESS = 'in_progress'
        # Answered = 'answered'

    category = models.ForeignKey(TicketCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    state = models.CharField(max_length=100, default=State.IN_PROGRESS, choices=State.choices)

    def __str__(self):
        return self.student.user.phone


class Message(models.Model):
    class Sender(models.TextChoices):
        STUDENT = 'student'
        ADMIN = 'admin'

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000, null=False)
    sender = models.CharField(max_length=20, default=Sender.STUDENT, choices=Sender.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
