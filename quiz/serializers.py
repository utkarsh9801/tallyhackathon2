from rest_framework import serializers
from quiz.models import Quiz
from quizapi.models import scoreModel


class scoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = scoreModel
        fields = '__all__'
