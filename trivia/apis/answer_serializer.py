from rest_framework import serializers
from trivia.apis.player_serializer import PlayerSerializer
from trivia.models import Answer, Choice, Player
from trivia.apis.choice_serializer import ChoiceSerializer


class AnswerSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)

    class Meta:
        model = Answer

        fields = (
            'id',
            'player',
            'round',
            'choice',
            'correct_answer',
            'create_date',
        )

    # Before we save this answer, need to calculate the correct_answer field
    def create(self, validated_data):

        answer = Answer(**validated_data)
        choice = answer.choice
        round = answer.round
        question = round.question
        choices = Choice.objects.filter(question=question).all()
        correct_choice = [choice for choice in choices if choice.correct_answer][0]
        user_id = self.context['request'].user.id
        # Only one player if a game and user are determined
        player = Player.objects.filter(game__rounds__in=[round.id], user=user_id).first()
        answer.player = player

        answer.correct_answer = choice.id == correct_choice.id

        answer.save()
        return answer
