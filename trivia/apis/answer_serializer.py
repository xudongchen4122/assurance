from rest_framework import serializers
from trivia.models import Answer
from trivia.apis.choice_serializer import ChoiceSerializer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = (
            'id',
            'player',
            'round',
            'choice',
            'create_date',
        )

    def create(self, validated_data):

        answer = Answer(**validated_data)
        choice = answer.choice
        round = answer.round
        question = round.question
        choices = question.choices
        correct_choice = [choice for choice in choices if choice.correct_answer][0]


        answer.save()
        return answer
