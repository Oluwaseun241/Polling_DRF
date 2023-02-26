from rest_framework import serializers
from .models import Poll

class PollSerializers(serializers.Serializers):
    id = model.IntegerField(read_only=True)
    question = models.CharField(max_length=250)

class AnswerSerializers(serializers.Serializers):
    pass
