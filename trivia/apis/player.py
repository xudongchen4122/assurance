from django.db.models import Q
from rest_framework import generics
from trivia.models import Player
from trivia.apis.player_serializer import PlayerSerializer


class PlayerList(generics.ListCreateAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        game = self.request.query_params.get('game', None)
        status = self.request.query_params.get('status', None)
        query_filter = None

        if game is not None:
            query_filter = Q(game=game)
        if status is not None:
            if query_filter is not None:
                query_filter &= Q(status=str(status).upper())
            else:
                query_filter = Q(status=str(status).upper())

        if query_filter is not None:
            q_set = Player.objects.filter(query_filter).all()
        else:
            q_set = Player.objects.all()
        return q_set
