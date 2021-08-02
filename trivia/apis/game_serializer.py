from rest_framework import serializers
from trivia.models import Game, Question, Round
import random


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = (
            'id',
            'name',
            'create_date',
        )

    def create(self, validated_data):
        game = Game(**validated_data)
        game.save()
        self._create_rounds(game)
        return game

    def _create_rounds(self, game):

        questions = list(Question.objects.all())
        random_questions = random.choices(questions, k=5)

        for i in range(len(random_questions)):
            question = random_questions[i]
            new_round = Round (
                game=game,
                question=question,
                order=i+1
            )
            new_round.save()
