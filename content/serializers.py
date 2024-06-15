from rest_framework import serializers

from content.models import ContentCategory, Content, Exam, ContentAccess, Chapter, Comment
from django.utils import timezone

from users.serializers import GetStudentInfoSerializer


class CommentSerializer(serializers.ModelSerializer):
    student = GetStudentInfoSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'


class ContentCategorySerializer(serializers.ModelSerializer):
    has_access = serializers.SerializerMethodField('get_access')
    chapters = serializers.SerializerMethodField('get_chapters')
    comments = serializers.SerializerMethodField('get_comments')

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

    @staticmethod
    def get_chapters(self):
        chapters = Chapter.objects.filter(category=self)
        return ChapterSerializer(chapters, many=True).data

    @staticmethod
    def get_comments(self):
        all_comments = Comment.objects.filter(category=self)
        return CommentSerializer(all_comments, many=True).data

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
