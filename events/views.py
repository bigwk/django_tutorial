from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


# Create your views here.
# generic views
class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'events/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'events/results.html'


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('events/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # output = '<br> '.join([q.question_text for q in latest_question_list])
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question Does Not Exist.')
    # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'events/detail.html', context={'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # response = 'You are looking at the results of question %s.'
    return render(request, 'events/results.html', context={'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'events/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('events:results', args=(question.id,)))
    # response = 'You are voting on question {}'.format(question_id)
    # return HttpResponse(response)