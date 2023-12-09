from rest_framework import serializers

from users.models import CustomUser, Grade, Field, City, Student


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['phone']

    def save(self, **kwargs):
        user = CustomUser(phone=self.validated_data['phone'])
        user.save()
        return user


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['grade', 'field', 'city']

    def save(self, **kwargs):
        student = Student(user=self.context.get('user'),
                          grade=self.validated_data['grade'],
                          field=self.validated_data['field'],
                          city=self.validated_data['city'])
        student.save()

        if 'first_name' in self.validated_data:
            student.first_name = self.validated_data['first_name']
        if 'last_name' in self.validated_data:
            student.last_name = self.validated_data['last_name']
        student.save()
        return student


class GetStudentInfoSerializer(serializers.ModelSerializer):
    grade = GradeSerializer()
    field = FieldSerializer()
    city = CitySerializer()
    user = CustomUserSerializer()

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'grade', 'field', 'city', 'student_code', 'id', 'user']

