from rest_framework import generics
from trivia.models import Game
from trivia.apis.game_serializer import GameSerializer


class GameList(generics.ListCreateAPIView):
    serializer_class = GameSerializer

    def get_queryset(self):
        q_set = Game.objects.all()
        return q_set
