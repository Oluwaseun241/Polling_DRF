from rest_framework import generics, permissions
from .models import Poll, Answer
from .serializers import PollSerializer, AnswerSerializer, UserSerializer, RegisterSerializer, PollCreateSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

user_list = UserList.as_view()

class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

register_user = RegisterUser.as_view()

class PollList(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.AllowAny]
    
poll_list = PollList.as_view()

class PollCreate(generics.CreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

poll_create = PollCreate.as_view()

class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

poll_detail = PollDetail.as_view()


class AnswerCreate(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        poll_id = self.kwargs['pk']
        poll = get_object_or_404(Poll, pk=poll_id)
        serializer.save(poll=poll, user=self.request.user)

create_answer = AnswerCreate.as_view()



