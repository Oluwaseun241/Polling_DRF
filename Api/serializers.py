from rest_framework import serializers
from .models import Poll, Answer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Answer
        fields = ['id','poll','answer_text', 'user']
