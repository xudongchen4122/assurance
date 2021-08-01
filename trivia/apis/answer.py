from rest_framework import generics
from trivia.models import Answer
from trivia.apis.answer_serializer import AnswerSerializer


class AnswerList(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        q_set = Answer.objects.all()
        return q_set
