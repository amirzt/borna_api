from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from content.models import ContentCategory, Content, Exam, ContentAccess, Comment
from content.serializers import ContentCategorySerializer, ContentSerializer, ExamSerializer
from users.models import Student, Wallet


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_content_categories(request):
    if 'special' in request.data:
        categories = ContentCategory.objects.filter(is_special=True, )
    else:
        categories = ContentCategory.objects.filter(is_special=False)
    serializer = ContentCategorySerializer(categories, many=True,
                                           context={'student': Student.objects.get(user_id=request.user.id)})
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_content(request):
    content = Content.objects.filter(category=request.data['category'])
    serializer = ContentSerializer(content, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_exam(request):
    exams = Exam.objects.filter(lesson=request.data['lesson'], type=request.data['type'])
    serializer = ExamSerializer(exams, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_content_access(request):
    category = ContentCategory.objects.get(id=request.data['category'])
    student = Student.objects.get(user_id=request.user.id)
    wallet = Wallet.objects.get(student=student)
    if wallet.balance < category.price:
        return Response(status=status.HTTP_402_PAYMENT_REQUIRED, data={"message": "موجودی کیف پول شما کافی نیست"})

    else:
        access = ContentAccess(student=student,
                               category=category)
        access.save()

        wallet.balance -= category.price
        wallet.save()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_comment(request):
    comment = Comment(category_id=request.data['category'],
                      content=request.data['content'],
                      file=request.data['file'],
                      student=Student.objects.get(user_id=request.user.id))
    comment.save()
    return Response(status=status.HTTP_200_OK)
