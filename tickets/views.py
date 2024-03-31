from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from tickets.models import TicketCategory, Ticket, Message
from tickets.serializers import TicketCategorySerializer, AddTicketSerializer, GetTicketSerializer, \
    GetMessageSerializer, AddMessageSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_categories(request):
    categories = TicketCategory.objects.all()
    serializer = TicketCategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_ticket(request):
    serializer = AddTicketSerializer(data=request.data,
                                     context={'user': request.user,
                                              'content': request.data['content']})
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Ticket added successfully'})
    return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tickets(request):
    tickets = Ticket.objects.filter(student__user=request.user)
    serializer = GetTicketSerializer(tickets, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_messages(request):
    messages = Message.objects.filter(ticket_id=request.data['ticket'])
    serializer = GetMessageSerializer(messages, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_message(request):
    serializer = AddMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Message added successfully'})
    return Response(serializer.errors, status=400)

