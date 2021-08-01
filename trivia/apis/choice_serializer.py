from rest_framework import serializers
from trivia.models import Choice


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = (
            'id',
            'description',
            'correct_answer',
            'question'
        )