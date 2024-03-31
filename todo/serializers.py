from rest_framework import serializers

from todo.models import Task
from users.models import Student


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'time', 'priority', 'time']

    def save(self, **kwargs):
        task = Task(student=Student.objects.get(user=self.context.get('user')),
                    title=self.validated_data['title'],
                    description=self.validated_data['description'],
                    time=self.validated_data['time'],
                    priority=self.validated_data['priority'])
        task.save()
        return task


class GetTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'