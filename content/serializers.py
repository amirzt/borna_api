from rest_framework import serializers

from content.models import ContentCategory, Content, Exam, ContentAccess
from django.utils import timezone


class ContentCategorySerializer(serializers.ModelSerializer):
    has_access = serializers.SerializerMethodField('get_access')

    def get_access(self, param):
        if param.is_clone:
            student = self.context.get('student')
            return False if student.expire_date < timezone.now() else True
        else:
            access = ContentAccess.objects.filter(student=self.context.get('student'),
                                                  category=param)

            if access.count() == 0:
                return False
            else:
                return True

    class Meta:
        model = ContentCategory
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'
