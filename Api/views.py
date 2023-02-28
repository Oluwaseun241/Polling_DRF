from rest_framework import generics, permissions, status
from rest_framework.exceptions import PermissionDenied
from .models import Poll, Answer
from .serializers import PollSerializer, AnswerSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

@api_view(['POST'])
def registration_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)
 
# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer


class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

PollList = PollList.as_view()

class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

PollDetail = PollDetail.as_view()

class AnswerPoll(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        poll = Poll.objects.get(pk=pk)
        if poll:
            serializer = AnswerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, poll=poll)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class DeletePoll(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        poll = Poll.objects.get(pk=pk)
        if poll:
            if poll.user == request.user:
                poll.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                raise PermissionDenied()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

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
