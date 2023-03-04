from rest_framework import generics, permissions, status
from .models import Poll, Answer
from .serializers import PollSerializer, AnswerSerializer, UserSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication



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

class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.AllowAny]

poll_list = PollList.as_view()

class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

poll_detail = PollDetail.as_view()


class AnswerCreate(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def create(self, request, *args, **kwargs):
        poll_id = self.kwargs.get('poll_id')

        try:
            poll = Poll.objects.get(pk=poll_id)
        except Poll.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user = request.user

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(poll=poll, user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
            
create_answer = AnswerCreate.as_view()


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
