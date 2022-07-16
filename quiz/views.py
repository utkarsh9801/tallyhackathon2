from django.shortcuts import render
from quiz.models import Quiz
from quizapi.serializers import QuizApiSerializer
from .models import scoreModel
from .serializers import scoreSerializer



def qpage(request):
	questions = Quiz.objects.all()

	return render(request, 'quiz.html', { 'questions': questions})


def result(request):
	def post(self, request, pk):
		username = request.user.username
		data = {'username': username, 'score': pk}
		serializer = scoreSerializer(data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
	return render(request, 'result.html')

	
	
