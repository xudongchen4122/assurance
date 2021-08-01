from rest_framework import generics
from trivia.models import Question
from trivia.apis.question_serializer import QuestionSerializer


class QuestionList(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        q_set = Question.objects.all()
        return q_set
