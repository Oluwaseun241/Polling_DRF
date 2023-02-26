from rest_framework import serializers
from .models import Poll

class PollSerializers(serializers.ModelSerializers):
    class Meta:
        model = Poll
        fields = '__all__'

class AnswerSerializers(serializers.ModelSerializers):
    class Meta:
        model = Answer
        fields = '__all__'
