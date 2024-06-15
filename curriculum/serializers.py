from rest_framework import serializers

from curriculum.models import CurriculumItem, CurriculumCategory, AdvisorPlan
from lessons.serializers import LessonSerializer


class GetCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurriculumCategory
        fields = '__all__'


class AddCurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurriculumItem
        fields = ['category', 'lesson', 'time', 'date', 'test_count', 'question_count']

    def save(self, **kwargs):
        item = CurriculumItem(category=self.validated_data['category'],
                              lesson=self.validated_data['lesson'],
                              time=self.validated_data['time'],
                              # grade=self.validated_data['grade'],
                              student=self.context['student'],
                              date=self.validated_data['date'])
        item.save()
        if 'test_count' in self.validated_data:
            item.test_count = self.validated_data['test_count']
        if 'question_count' in self.validated_data:
            item.question_count = self.validated_data['question_count']
        item.save()

        return item


class GetCurriculumSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()
    category = GetCategoriesSerializer()

    class Meta:
        model = CurriculumItem
        fields = '__all__'


class AddPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvisorPlan
        fields = ['category', 'lesson', 'time', 'date', 'test_count', 'question_count']

    def save(self, **kwargs):
        item = AdvisorPlan(category=self.validated_data['category'],
                           lesson=self.validated_data['lesson'],
                           time=self.validated_data['time'],
                           advisor=self.context.get('advisor'),
                           student=self.context['student'],
                           date=self.validated_data['date'])
        item.save()
        if 'test_count' in self.validated_data:
            item.test_count = self.validated_data['test_count']
        if 'question_count' in self.validated_data:
            item.question_count = self.validated_data['question_count']
        item.save()

        return item


class GetPlanSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()
    category = GetCategoriesSerializer()

    class Meta:
        model = AdvisorPlan
        fields = '__all__'
