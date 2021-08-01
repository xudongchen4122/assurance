from rest_framework import serializers
from trivia.models import Question


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = (
            'id',
            'description'
        )