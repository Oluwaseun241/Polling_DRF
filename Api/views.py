from rest_framework import generics, permissions, status
from .models import Poll, Answer
from .serializers import PollSerializer, AnswerSerializer, UserSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

class UserList(generics.ListAPIView):
    authentication_class = (TokenAuthentication)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

UserList = UserList.as_view()

class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

RegisterUser = RegisterUser.as_view()

class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

PollList = PollList.as_view()

class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

PollDetail = PollDetail.as_view()

# Function based views
# @api_view(['GET', 'POST'])
# def poll_list(request):
#     if request.method == 'GET':
#         polls = Poll.objects.all()
#         serializer = PollSerializer(polls, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PollSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
