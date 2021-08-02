from rest_framework import generics
from trivia.models import Answer
from trivia.apis.answer_serializer import AnswerSerializer


class AnswerList(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        round_id = self.request.query_params.get('round', None)

        if round_id is not None:
            q_set = Answer.objects.filter(round=round_id).prefetch_related('player').all()
        else:
            q_set = Answer.objects.prefetch_related('player').all()

        return q_set
