from rest_framework import serializers

from curriculum.models import CurriculumItem, Category


class GetCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AddCurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurriculumItem
        fields = ['category', 'lesson', 'time', 'grade', 'date']

    def save(self, **kwargs):
        item = CurriculumItem(category=self.validated_data['category'],
                              lesson=self.validated_data['lesson'],
                              time=self.validated_data['time'],
                              grade=self.validated_data['grade'],
                              student=self.context['student'],
                              date=self.validated_data['date'])
        item.save()
        if 'question_type' in self.validated_data:
            item.question_type = self.validated_data['question_type']
        if 'question_count' in self.validated_data:
            item.question_count = self.validated_data['question_count']
        if 'test_type' in self.validated_data:
            item.test_type = self.validated_data['test_type']
        item.save()

        return item


class GetCurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurriculumItem
        fields = '__all__'
