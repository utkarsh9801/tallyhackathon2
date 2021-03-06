from rest_framework import serializers
from quiz.models import Quiz
from quizapi.models import scoreModel

class QuizApiSerializer(serializers.ModelSerializer):

	class Meta:
		model = Quiz
		fields = '__all__'


class scoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = scoreModel
		fields = '__all__'
