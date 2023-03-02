from rest_framework import serializers
from .models import Poll, Answer
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['id', 'username', 'email']
        
# class RegisterSerializer(serializers.ModelSerializer):
#     username = serializers.UsernameField(required=True)
#     email = serializers.EmailField


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Answer
        fields = ['id','poll','answer_text', 'user']
