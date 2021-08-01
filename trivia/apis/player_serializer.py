from rest_framework import serializers
from trivia.models import Player


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = (
            'id',
            'game',
            'user',
            'last_round',
            'create_date',
            'update_date',
        )

