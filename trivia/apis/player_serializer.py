from rest_framework import serializers
from trivia.models import Player
from django.contrib.auth.models import User


class PlayerSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = (
            'id',
            'game',
            'user',
            'username',
            'last_round',
            'create_date',
            'update_date',
        )

    @staticmethod
    def get_username(player):
        user = User.objects.filter(pk=player.user_id).first()
        return None if user is None else user.username
