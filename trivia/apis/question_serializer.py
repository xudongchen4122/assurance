from rest_framework import serializers
from trivia.models import Question


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = (
            'id',
            'description'
        )

    def create(self, validated_data):
        # Check if description is empty
        if validated_data['description'].strip == '':
            raise Exception('question.description cannot be whitespace')

        question = Question(**validated_data)
        question.save()
        return question
