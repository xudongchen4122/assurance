from rest_framework import serializers
from trivia.models import Player
from django.contrib.auth.models import User


class PlayerSerializer(serializers.ModelSerializer):

    # We need to return username to the frontend so that it could be displayed.
    # However, this username doesn't exist in player object, so we need to
    # call a static method to calculate it
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
