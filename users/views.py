import json

# from celery.worker.state import requests
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from users.models import Grade, Field, City, Student, Banner, TutorialVideo, University, UniversityTarget, CustomUser, \
    OTP
from users.serializers import GradeSerializer, FieldSerializer, CitySerializer, CustomUserSerializer, StudentSerializer, \
    GetStudentInfoSerializer, UniversitySerializer, BannerSerializer, TutorialSerializer, AddAdvisorRequest

import requests


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


def send_otp(otp, phone):
    api_url = "https://api2.ippanel.com/api/v1/sms/webservice/single"

    headers = {
        'Content-Type': 'application/json',
        'apikey': 'Bearer M-o-KUXHu_VfZgtr6dzrptzXjq0GFeZcoT5pV2PCc34='
    }

    body = {
        "recipient": [
            phone
        ],
        "sender": "+983000505",
        # "time": "2025-03-21T09:12:50.824Z",
        "message": "کد وورد به نرم افزار مشاورسرا \n "+otp+"\n لغو11"
    }
    response = requests.post(api_url, headers=headers, data=json.dumps(body))
    print(response)


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    try:
        user = CustomUser.objects.get(phone=request.data['phone'])
        user.is_active = True
        user.save()

        token, created = Token.objects.get_or_create(user=user)

        otp = OTP(user=user)
        otp.save()
        send_otp(otp.code, user.phone)

        return Response({
            'token': token.key,
            'exist': True
        }, status=200)

    except CustomUser.DoesNotExist:
        user_serializer = CustomUserSerializer(data=request.data)

        if user_serializer.is_valid():
            user = user_serializer.save()

            otp = OTP(user=user)
            otp.save()
            send_otp(otp.code, user.phone)

            token, created = Token.objects.get_or_create(user=user)


            return Response({
                'token': token.key,
                'exist': False
            })

        else:
            return Response(user_serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_otp(request):
    otp = OTP.objects.filter(user=request.user).last()
    if otp.code == request.data['code']:
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


def get_student_code(grade):
    chars = '1234567890'
    random_code = get_random_string(length=4, allowed_chars=chars)
    code = "402"+grade+random_code
    return code


@api_view(['POST'])
@permission_classes([AllowAny])
def add_student(request):
    user = CustomUser.objects.get(phone=request.data['phone'])
    student_serializer = StudentSerializer(data=request.data, context={'user': user})
    if student_serializer.is_valid():
        student = student_serializer.save()
        student.student_code = get_student_code(student.grade.code)
        student.save()

        user.is_active = True
        user.save()

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
        }, status=200)
    else:
        return Response(student_serializer.errors, status=400)


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
    if 'image' in request.data:
        student.image = request.data['image']
    student.save()
    return Response(status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_universities(request):
    universities = University.objects.all()
    return Response(UniversitySerializer(universities, many=True).data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_target(request):
    try:
        target = UniversityTarget.objects.get(student__user=request.user)
        target.delete()
    except UniversityTarget.DoesNotExist:
        pass

    new_target = UniversityTarget(student=Student.objects.get(user=request.user),
                                  university_id=request.data['university'])
    new_target.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_home(request):
    banner = Banner.objects.filter(is_active=True).last()
    tutorial = TutorialVideo.objects.filter().last()
    student = Student.objects.get(user=request.user)
    target = UniversityTarget.objects.filter(student__user=request.user).last().university

    data = {
        'banner': BannerSerializer(banner).data,
        'tutorial': TutorialSerializer(tutorial).data,
        'student': GetStudentInfoSerializer(student).data,
        'target': UniversitySerializer(target).data
    }
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def advisor_request(request):
    serializer = AddAdvisorRequest(data=request.data,
                                   context={'user': request.user})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
