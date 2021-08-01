from rest_framework import generics
from trivia.models import Choice
from trivia.apis.choice_serializer import ChoiceSerializer


class ChoiceList(generics.ListCreateAPIView):
    serializer_class = ChoiceSerializer

    def get_queryset(self):
        q_set = Choice.objects.all()
        return q_set
