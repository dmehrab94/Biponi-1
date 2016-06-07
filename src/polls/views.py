from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
#from django.db import models
from .models import Choice,Question #ei line ta dekhe ami djangor fan hoia gelam
# Create your views here.
def  index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request,'polls/index.html',context)

def detail(request,question_id):
	try:
		q=Question.objects.get(pk=question_id)
		context={
			'question': q,
		}
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request,'polls/detail.html',context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

	

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'polls/results.html', {'question':question})
		#return render(request, 'polls/results.html', {})