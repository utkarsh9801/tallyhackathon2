from django.conf.urls import url
import quiz.views as quiz_views

urlpatterns = [
	url(r'^$', quiz_views.qpage),
	#create a new urk pattern result to the url /quiz/result
	url(r'^result/<str:pk>/', quiz_views.result, name='result'),

	
]
