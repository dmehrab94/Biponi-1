from django.conf.urls import url

from . import views
#all urls starts with /polls/ here

urlpatterns=[
	url(r'^$',views.index,name='index'),
	# /polls/5/ at least one number thats why [0-9]+
	url(r'^(?P<question_id>[0-9]+)/$',views.detail, name='detail'),
	# /polls/5/results
	url(r'^(?P<question_id>[0-9]+)/results/$',views.results, name='result'),
	url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote, name='vote'),
]