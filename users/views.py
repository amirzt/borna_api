from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from users.models import Grade, Field, City, Student
from users.serializers import GradeSerializer, FieldSerializer, CitySerializer, CustomUserSerializer, StudentSerializer, \
    GetStudentInfoSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_grade(request):
    grades = Grade.objects.all()
    serializer = GradeSerializer(grades, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_field(request):
    fields = Field.objects.all()
    serializer = FieldSerializer(fields, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_city(request):
    cities = City.objects.all()
    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    user_serializer = CustomUserSerializer(data=request.data)

    if user_serializer.is_valid():
        user = user_serializer.save()
        student_serializer = StudentSerializer(data=request.data, context={'user': user})
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(user_serializer.data, status=200)
        else:
            return Response(student_serializer.errors, status=400)
    else:
        return Response(user_serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_student_info(request):
    student = Student.objects.get(user=request.user)
    serializer = GetStudentInfoSerializer(student)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_student_info(request):
    student = Student.objects.get(user=request.user)
    if 'first_name' in request.data:
        student.first_name = request.data['first_name']
    if 'last_name' in request.data:
        student.last_name = request.data['last_name']
    if 'grade' in request.data:
        student.grade = Grade.objects.get(id=request.data['grade'])
    if 'field' in request.data:
        student.field = Field.objects.get(id=request.data['field'])
    if 'city' in request.data:
        student.city = City.objects.get(id=request.data['city'])
    student.save()
    return Response(status=200)
