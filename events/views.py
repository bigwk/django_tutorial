from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    request_str = str(type(request))
    requests = dir(request)
    request_str += '。'.join(requests)
    # request_str = request.headers
    # request_str = request.read()
    return HttpResponse(request_str)

def detail(request, question_id):
    return HttpResponse('You are looking at question %s.' % question_id)

def results(request, question_id):
    response = 'You are looking at the results of question %s.'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    response = 'You are voting on question {}'.format(question_id)
    return HttpResponse(response)